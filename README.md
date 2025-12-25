# Google Play Store Review Trend Analysis AI Agent

## Overview
This project implements an agentic AI system that analyzes Google Play Store reviews
(Zomato app) to identify user issues, requests, and feedback trends over time.

The system processes reviews in daily batches and generates a rolling 30-day trend
report showing the frequency of each topic.

## Features
- Daily ingestion of Play Store reviews
- LLM-based semantic topic extraction
- Automatic topic normalization
- Rolling T-30 to T trend analysis
- CSV output for product insights

## Architecture
1. Review Fetching Agent
2. Topic Extraction Agent (LLM-based)
3. Trend Aggregation Agent

## Tech Stack
- Python
- google-play-scraper
- OpenAI API
- Pandas

## How to Run
```bash
python fetch_reviews.py
python llm_topic_extractor.py
python build_trend_table.py
