# Lab-Buddy

## About
A simple web-app that facilitates the students with links to resources and tutorials for the common problems.

## Getting Started

1. Install docker and docker-compose - https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=94798094
2. From the project root, run the command - `docker-compose up --build`
   To run in detached mode use the following commands:
   ```
   docker-compose build
   docker-compose up -d
   ```
   This starts the docker container in background. To see the container logs run:
   ```
   docker-compose logs -f
   ```
3. The API will start listening at  - http://0.0.0.0:9898/

## Requirements

- Main page UI for all the topics and their sub-topics.
- Database connection API for fetching the URL corresponding to the topic id.
- Each topic will be mapped to an unique-id in the database.
- SQLite connection.
