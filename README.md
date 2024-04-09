Build and run the Docker containers:

docker-compose up --build (run with sudo in linux)

This setup will create a persistent PostgreSQL database volume and use it to store the video data. The Flask application will connect to the database using the environment variables defined in the docker-compose.yml file.
When you start the containers, the database will be initialized, and the Flask application will be able to interact with the persistent PostgreSQL database.