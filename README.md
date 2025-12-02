# Sentiment-Analysis Project

## Overview

This project focuses on analyzing depression-related content on Twitter to identify **patterns**, **sentiments**, and **topics**. It is powered by a FastAPI backend with the following capabilities:

* Scrapes tweets using the Twitter API
* Cleans and normalizes text data
* Performs sentiment analysis using Hugging Face's DistilBERT
* Detects topics through rule-based keyword matching
* Stores results in MongoDB for access and visualization

---

## Key Features

* Twitter data scraping with support for one or multiple Bearer Tokens (with rotation and rate limit handling)
* Comprehensive text preprocessing: cleaning, normalization, and stopword removal
* Sentiment classification using a pre-trained DistilBERT model
* Rule-based topic detection
* RESTful API for initiating scraping and retrieving results
* Asynchronous background processing using FastAPI

---

## Installation and Setup

### Requirements

* Python 3.8 or higher
* One or more Twitter API Bearer Tokens
* Docker and Docker Compose

### Quickstart

1. Clone the repository:

   ```bash
   git clone https://github.com/YoussefNKH/Sentiment-Analysis.git
   cd sentiment-analysis
   ```

2. Create a `.env` file and add your Twitter API Bearer Tokens:

   ```env
   TWITTER_BEARER_TOKEN_1=your_first_token
   TWITTER_BEARER_TOKEN_2=your_second_token
   ```

   The system will automatically rotate between multiple tokens to handle rate limits. If only `TWITTER_BEARER_TOKEN` is present, it will be used as the default.

---

## Running the Application with Docker Compose

To build and start the application:

```bash
docker-compose up --build
```

To run in the background:

```bash
docker-compose up -d
```

Check the status of the running containers:

```bash
docker-compose ps
```

Once running, open your browser and visit:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoints

| Method | Endpoint      | Description                                |
| ------ | ------------- | ------------------------------------------ |
| POST   | `/api/scrape` | Initiates asynchronous Twitter scraping    |
| GET    | `/api/posts`  | Retrieves all processed posts from MongoDB |

---

## Testing

To run unit tests:

```bash
python -m pytest tests/
```

Test cases cover:

* URL and emoji removal
* Text normalization
* Stopword removal
* Edge cases in preprocessing logic

---

## Project Structure

```
sentiment-analysis/
├── app/
│   ├── main.py                 # Application entry point
│   ├── api/endpoints.py        # REST API route definitions
│   ├── database/mongodb.py     # MongoDB connection handling
│   ├── nlp/
│   │   ├── sentiment_analysis.py
│   │   ├── text_processing.py
│   │   └── topic_detection.py
│   ├── core/config.py
│   └── scraper/twitter_scraper.py
└── tests/
    └── test_text_processor.py
```