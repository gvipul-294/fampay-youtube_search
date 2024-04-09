import requests
import threading
# from app import app
# from kafka_impl import producer, consumer, KAFKA_TOPIC
# from flask import jsonify, json

# # Set up a route to trigger the async fetch of latest videos
# @app.route('/async', methods=['GET'])
# def fetch_latest_videos_async_api():
#     try:
#         producer.send(KAFKA_TOPIC, {'action': 'fetch_latest_videos_sync'})
#         return jsonify({'message': 'Latest videos fetch request sent to Kafka'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
# def fetch_latest_videos_kafka_handler():
#     for msg in consumer:
#         try:
#             data = json.loads(msg.value)
#             if data['action'] == 'fetch_latest_videos_sync':
#                 response = requests.get('http://localhost:5000/')
#                 if response.status_code == 200:
#                     print(response.json()['message'])
#                 else:
#                     print(f"Error fetching latest videos: {response.json()['error']}")
#         except Exception as e:
#             print(f"Error fetching latest videos: {e}")
#         threading.Timer(10.0, fetch_latest_videos_kafka_handler).start()

def fetch_latest_videos_handler():
    try:        
        response = requests.get('http://localhost:5000/')
        if response.status_code == 200:
            print(response.json()['message'])
        else:
            print(f"Error fetching latest videos: {response.json()['error']}")
    except Exception as e:
        print(f"Error fetching latest videos: {e}")

def start_background_task():
    threading.Timer(10.0, start_background_task).start()
    # fetch_latest_videos_async_api()
    fetch_latest_videos_handler()
