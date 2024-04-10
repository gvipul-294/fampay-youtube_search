Build and run the Docker containers:

docker-compose up --build (run with sudo in linux)

This setup will create a persistent PostgreSQL database volume and use it to store the video data. The Flask application will connect to the database using the environment variables defined in the docker-compose.yml file.
When you start the containers, the database will be initialized, and the Flask application will be able to interact with the persistent PostgreSQL database.

Example request
http://localhost:5000/search?title=2024&description=CSK

{
  "data": [
    {
      "description": "IPL 2024 Match 23 Punjab Kings vs Sunrisers Hyderabad Live This Match Will be Played at Maharaja Yadavindra Singh ...",
      "id": 51,
      "published_at": "2024-04-09T18:43:39",
      "thumbnail_url": "https://i.ytimg.com/vi/8yjGu8r3rJg/default.jpg",
      "title": "IPL 2024 Live: Punjab Kings vs Sunrisers Hyderabad Live | PBKS vs SRH Live Scores &amp; Commentary"
    },
    {
      "description": "IPL 2024 Match 23 Punjab Kings vs Sunrisers Hyderabad Live This Match Will be Played at Maharaja Yadavindra Singh ...",
      "id": 1,
      "published_at": "2024-04-09T18:43:39",
      "thumbnail_url": "https://i.ytimg.com/vi/8yjGu8r3rJg/default.jpg",
      "title": "IPL 2024 Live: Punjab Kings vs Sunrisers Hyderabad Live | PBKS vs SRH Live Scores &amp; Commentary"
    },
    {
      "description": "IPL 2024 Match 23 Punjab Kings vs Sunrisers Hyderabad Live This Match Will be Played at Maharaja Yadavindra Singh ...",
      "id": 251,
      "published_at": "2024-04-09T18:43:39",
      "thumbnail_url": "https://i.ytimg.com/vi/8yjGu8r3rJg/default.jpg",
      "title": "IPL 2024 Live: Punjab Kings vs Sunrisers Hyderabad Live | PBKS vs SRH Live Scores &amp; Commentary"
    },
    {
      "description": "IPL 2024 Match 23 Punjab Kings vs Sunrisers Hyderabad Live This Match Will be Played at Maharaja Yadavindra Singh ...",
      "id": 401,
      "published_at": "2024-04-09T18:43:39",
      "thumbnail_url": "https://i.ytimg.com/vi/8yjGu8r3rJg/default.jpg",
      "title": "IPL 2024 Live: Punjab Kings vs Sunrisers Hyderabad Live | PBKS vs SRH Live Scores &amp; Commentary"
    },
    {
      "description": "IPL 2024 Match 23 Punjab Kings vs Sunrisers Hyderabad Live This Match Will be Played at Maharaja Yadavindra Singh ...",
      "id": 151,
      "published_at": "2024-04-09T18:43:39",
      "thumbnail_url": "https://i.ytimg.com/vi/8yjGu8r3rJg/default.jpg",
      "title": "IPL 2024 Live: Punjab Kings vs Sunrisers Hyderabad Live | PBKS vs SRH Live Scores &amp; Commentary"
    },
    {
      "description": "IPL 2024 Match 23 Punjab Kings vs Sunrisers Hyderabad Live This Match Will be Played at Maharaja Yadavindra Singh ...",
      "id": 101,
      "published_at": "2024-04-09T18:43:39",
      "thumbnail_url": "https://i.ytimg.com/vi/8yjGu8r3rJg/default.jpg",
      "title": "IPL 2024 Live: Punjab Kings vs Sunrisers Hyderabad Live | PBKS vs SRH Live Scores &amp; Commentary"
    },
    {
      "description": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores & Commentary | Punjab Kings vs Sunrisers Hyderabad | IPL ...",
      "id": 2,
      "published_at": "2024-04-09T18:43:10",
      "thumbnail_url": "https://i.ytimg.com/vi/Jut1qW1iJcI/default.jpg",
      "title": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores &amp; Commentary | IPL LIVE | 4 overs"
    },
    {
      "description": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores & Commentary | Punjab Kings vs Sunrisers Hyderabad | IPL ...",
      "id": 102,
      "published_at": "2024-04-09T18:43:10",
      "thumbnail_url": "https://i.ytimg.com/vi/Jut1qW1iJcI/default.jpg",
      "title": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores &amp; Commentary | IPL LIVE | 4 overs"
    },
    {
      "description": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores & Commentary | Punjab Kings vs Sunrisers Hyderabad | IPL ...",
      "id": 152,
      "published_at": "2024-04-09T18:43:10",
      "thumbnail_url": "https://i.ytimg.com/vi/Jut1qW1iJcI/default.jpg",
      "title": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores &amp; Commentary | IPL LIVE | 4 overs"
    },
    {
      "description": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores & Commentary | Punjab Kings vs Sunrisers Hyderabad | IPL ...",
      "id": 52,
      "published_at": "2024-04-09T18:43:10",
      "thumbnail_url": "https://i.ytimg.com/vi/Jut1qW1iJcI/default.jpg",
      "title": "Live: PBKS VS SRH, Chandigarh - IPL 2024, Match 23 | Live Scores &amp; Commentary | IPL LIVE | 4 overs"
    }
  ],
  "page": 1,
  "per_page": 10,
  "total": 319
}