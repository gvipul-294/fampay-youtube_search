# from dotenv import load_dotenv
import os
import datetime
from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from database.db import Session, init_db
from entity.video import Video

# Set up the Flask app
app = Flask(__name__)

# Initialize the database
init_db()

# Load environment variables from the .env file
# load_dotenv()

# Initialize the YouTube API client
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Background task to fetch the latest videos
@app.route('/', methods=['GET'])
def fetch_latest_videos_sync_api():
    search_query = 'ipl' # search query string (modifiable)
    published_after = (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat() + 'Z'

    try:
        response = youtube.search().list(
            forDeveloper=True,
            part='id,snippet',
            type='video',
            order='date',
            q=search_query,
            publishedAfter=published_after,
            maxResults=200
        ).execute()

        for item in response['items']:
            video = Video(
                title=item['snippet']['title'],
                description=item['snippet']['description'],
                published_at=datetime.datetime.strptime(item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                thumbnail_url=item['snippet']['thumbnails']['default']['url']
            )
            session = Session()
            session.add(video)
            session.commit()
            session.close()
        
        return jsonify({'message': 'Latest videos fetched and stored in database.'}), 200

    except HttpError as e:
        return jsonify({'error': str(e)}), 500

# Set up a route to fetch the latest videos in a paginated response
@app.route('/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page

    session = Session()
    videos = session.query(Video).order_by(Video.published_at.desc()).offset(offset).limit(per_page).all()
    total_videos = session.query(Video).count()
    session.close()

    return jsonify({
        'data': [v.to_dict() for v in videos],
        'total': total_videos,
        'page': page,
        'per_page': per_page
    })

# Set up a route for the search API
@app.route('/search', methods=['GET'])
def search_videos():
    title = request.args.get('title', '')
    description = request.args.get('description','')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page

    session = Session()
    videos = session.query(Video).filter(
        Video.title.like(f'%{title}%') | Video.description.like(f'%{description}%')
    ).order_by(Video.published_at.desc()).offset(offset).limit(per_page).all()

    total_videos = session.query(Video).filter(
        Video.title.like(f'%{title}%') | Video.description.like(f'%{description}%')
    ).count()
    session.close()

    return jsonify({
        'data': [v.to_dict() for v in videos],
        'total': total_videos,
        'page': page,
        'per_page': per_page
    })