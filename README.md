# 🛰️ TruthStream: Real-Time Fake News Detection Pipeline

TruthStream is an end-to-end fake news detection system designed to ingest live data from Reddit and News APIs, process and classify it in real time, and present insights through an interactive Streamlit dashboard. The pipeline integrates Kafka for streaming, MongoDB for storage, Hugging Face's BERT for classification, and optional Wikidata-based verification for added trust evaluation.

---

## 📌 Table of Contents

- [🧠 Overview](#-overview)
- [⚙️ Architecture](#️-architecture)
- [🌟 Key Features](#-key-features)
- [📁 Project Structure](#-project-structure)
- [🛠️ Setup and Installation](#️-setup-and-installation)
- [🚀 Usage Guide](#-usage-guide)
- [🔧 APIs & Configuration](#-apis--configuration)
- [🧪 Model Training](#-model-training)
- [✅ Testing](#-testing)
- [⚠️ Limitations and Improvements](#️-limitations-and-improvements)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## 🧠 Overview

TruthStream tackles real-time misinformation by combining:

- Real-time ingestion from **Reddit** and **NewsAPI**
- Stream processing via **Apache Kafka**
- Fake news classification using a **fine-tuned BERT model**
- Entity-level verification with **Wikidata**
- Storage in **MongoDB**
- A visual interface via **Streamlit**

This system demonstrates how scalable NLP and streaming tools can power misinformation monitoring solutions for journalism, research, and content moderation.

---

## ⚙️ Architecture

```text
         ┌────────────────────────────────────┐
         │          Data Sources              │
         │ ┌────────────┐  ┌────────────────┐ │
         │ │ Reddit API │  │  NewsAPI.org   │ │
         │ └─────┬──────┘  └────────┬───────┘ │
         └───────┼─────────────────┼─────────┘
                 ↓                 ↓
         ┌────────────────────────────────────┐
         │       Ingestion Layer (src/)       │
         │  reddit_stream.py / newsapi_fetch.py│
         └────────────────────────────────────┘
                        ↓
         ┌────────────────────────────────────┐
         │     Kafka Streaming Pipeline       │
         │ kafka_producer.py / kafka_consumer.py │
         └────────────────────────────────────┘
                        ↓
         ┌────────────────────────────────────┐
         │     Preprocessing & Inference      │
         │  clean_text.py / predict.py        │
         └────────────────────────────────────┘
                        ↓
         ┌────────────────────────────────────┐
         │  Verification (Wikidata optional)  │
         │ verify_with_wikidata.py            │
         └────────────────────────────────────┘
                        ↓
         ┌────────────────────────────────────┐
         │       Storage (MongoDB)            │
         │ save_to_mongo.py                   │
         └────────────────────────────────────┘
                        ↓
         ┌────────────────────────────────────┐
         │      Streamlit Dashboard (UI)      │
         │         dashboard/app.py           │
         └────────────────────────────────────┘
```

---

## 🌟 Key Features

- ✅ Real-time stream ingestion from Reddit & NewsAPI
- ✅ Kafka-based producer-consumer architecture
- ✅ BERT-based classification of fake/real news
- ✅ Optional knowledge verification using Wikidata
- ✅ MongoDB integration for historical tracking
- ✅ Intuitive Streamlit dashboard for visualization
- ✅ Modular, production-ready codebase

---

## 📁 Project Structure

```text
truthstream/
├── data/
│   ├── raw/                  
│   ├── labeled/              
│   └── sources.md            
│
├── models/
│   └── bert_fake_news_classifier.pkl
│
├── src/
│   ├── ingestion/
│   │   ├── reddit_stream.py
│   │   ├── newsapi_fetch.py
│   │   └── simulate_stream.py
│   ├── kafka/
│   │   ├── kafka_producer.py
│   │   └── kafka_consumer.py
│   ├── preprocessing/
│   │   └── clean_text.py
│   ├── model/
│   │   ├── train_model.py
│   │   └── predict.py
│   ├── verification/
│   │   ├── verify_with_wikidata.py
│   │   └── entity_linking.py
│   ├── storage/
│   │   ├── save_to_mongo.py
│   │   └── schema_example.json
│   └── dashboard/
│       └── app.py
│
├── notebooks/
│   ├── data_exploration.ipynb
│   └── model_training.ipynb
│
├── config/
│   └── config.yaml
├── tests/
│   ├── test_cleaning.py
│   ├── test_model.py
│   └── test_pipeline.py
├── requirements.txt
├── README.md
├── architecture.png
└── .env
```

---

## 🛠️ Setup and Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/truthstream.git
cd truthstream
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Kafka & MongoDB Setup

Make sure these services are running:

- **Kafka**: https://kafka.apache.org/quickstart
- **MongoDB**: `sudo service mongod start` or use Docker

---

## 🚀 Usage Guide

### 1. Start Data Ingestion

```bash
python src/ingestion/reddit_stream.py
python src/ingestion/newsapi_fetch.py
```

Or simulate the stream:

```bash
python src/ingestion/simulate_stream.py
```

### 2. Launch Kafka Producer & Consumer

```bash
python src/kafka/kafka_producer.py
python src/kafka/kafka_consumer.py
```

### 3. Run the Streamlit Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## 🔧 APIs & Configuration

Update `config/config.yaml`:

```yaml
reddit:
  client_id: YOUR_ID
  client_secret: YOUR_SECRET
  user_agent: truthstream-bot

newsapi:
  api_key: YOUR_NEWSAPI_KEY

mongodb:
  uri: mongodb://localhost:27017
  database: truthstream
```

Set sensitive values in `.env` and use `dotenv` to load.

---

## 🧪 Model Training

To retrain or fine-tune the model:

```bash
python src/model/train_model.py
```

Explore experiments in:

```bash
notebooks/model_training.ipynb
```

---

## ✅ Testing

Run all unit tests:

```bash
pytest tests/
```

Includes tests for:

- Preprocessing logic
- Prediction pipeline
- Stream sanity checks

---

## ⚠️ Limitations and Improvements

### ❗ Limitations

- Wikidata verification is not fully real-time
- May misclassify satire or low-resource languages
- Dashboard lacks explainability insights

### 🔮 Future Enhancements

- SHAP explainability for BERT predictions
- Multilingual news detection
- Docker + Kubernetes deployment
- Whisper + CLIP for multimedia fake news

---

## 📄 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for full details.

---

## 📬 Contact

**Author:** Siddheshwar Wagawad  
📧 Email: siddhwagawad@gmail.com  
🐙 GitHub: [@thesiddheshh](https://github.com/thesiddheshh)

---

```bash
# TruthStream — Real-time NLP pipeline for fake news detection.
# Apache Kafka | MongoDB | BERT | Streamlit | PRAW | NewsAPI
```
