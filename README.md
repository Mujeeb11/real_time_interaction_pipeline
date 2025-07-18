# 🚀 Real-Time User Interaction Pipeline

This project simulates user interaction data, processes it in real-time, stores the aggregations in MongoDB, and displays a real-time dashboard.

## 🔧 Tech Stack
- **Kafka** - Data streaming
- **MongoDB** - NoSQL database for aggregation storage
- **Streamlit** - Dashboard for real-time insights
- **Python** - Core language

## 📦 Project Structure
```
real_time_interaction_pipeline/
├── producer/
│   └── data_generator.py
├── consumer/
│   └── consumer_aggregator.py
├── dashboard/
│   └── app.py
├── config/
│   └── settings.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚦 Components

### 1. Data Generator & Kafka Producer
- Simulates random interaction events and pushes to Kafka.

### 2. Kafka Consumer & Aggregator
- Consumes messages from Kafka and performs aggregations in real-time.

### 3. NoSQL Storage (MongoDB)
- Stores aggregated metrics efficiently.

### 4. Streamlit Dashboard
- Displays real-time insights.

## 🏁 Getting Started

1. Start Kafka and MongoDB locally.
2. Run the producer:
```bash
python producer/data_generator.py
```
3. Run the consumer:
```bash
python consumer/consumer_aggregator.py
```
4. Launch the dashboard:
```bash
streamlit run dashboard/app.py
```