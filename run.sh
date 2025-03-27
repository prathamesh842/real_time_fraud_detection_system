#!/bin/bash

# Function to stop all containers
stop_containers() {
    echo "Stopping all containers..."
    docker-compose down
    exit 0
}

# Set up trap for Ctrl+C
trap stop_containers SIGINT SIGTERM

# Start all services
echo "Starting all services..."
docker-compose up -d

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 10

# Start producer in background
echo "Starting producer..."
docker-compose up producer &

# Start console consumer
echo "Starting console consumer..."
docker-compose up kafka-console-consumer

# When consumer is stopped, stop all containers
stop_containers 