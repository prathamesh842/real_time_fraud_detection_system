# Real-time Credit Card Fraud Detection

A real-time credit card fraud detection system using machine learning, Kafka, and Docker.

## Features

- Real-time transaction monitoring
- Machine learning-based fraud detection
- Kafka integration for stream processing
- Docker containerization
- Web interface for predictions

## Prerequisites

- Docker
- Docker Compose

## Project Structure

```
.
├── app.py                 # Main Flask application
├── project/
│   ├── producer.py       # Kafka producer for transactions
│   └── consumer.py       # Kafka consumer for processing
├── notebooks/            # Jupyter notebooks and trained models
├── templates/            # HTML templates
├── DATASET/             # Dataset files
├── docker-compose.yml   # Docker services configuration
├── Dockerfile          # Application container configuration
└── run.sh             # Automation script
```

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd real-time-credit-card-detection
```

2. Download the dataset:
   - Download the credit card fraud dataset from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)
   - Place the `creditcard.csv` file in the `DATASET` directory

3. Make the run script executable:
```bash
chmod +x run.sh
```

## Usage

1. Start the application:
```bash
./run.sh
```

This will:
- Start all required services (Zookeeper, Kafka, Flask app)
- Start the transaction producer
- Start the Kafka console consumer
- Open the web interface at http://localhost:5000

2. Monitor the system:
- View transactions in the console
- Check predictions at http://localhost:5000
- Monitor fraudulent transactions in the logs

3. Stop the application:
- Press Ctrl+C in the terminal where run.sh is running
- All services will be stopped automatically

## API Endpoints

- `GET /`: Home page with prediction form
- `POST /predict`: Endpoint for fraud detection predictions

## Development

To modify the application:

1. Make changes to the source code
2. Rebuild the containers:
```bash
docker-compose up --build
```

## License

[Your chosen license]

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 