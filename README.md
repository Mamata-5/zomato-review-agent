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
AI Validation & Quality Assurance
## AI Validation & Quality Assurance

To ensure the correctness and reliability of the AI agent, multiple validation
checks were performed during development:

### 1. Manual Review-to-Topic Verification
Random samples of raw Play Store reviews were manually compared with the
AI-extracted topics to verify semantic correctness.

Example:
Review:
"The delivery partner was rude and food arrived cold."

Extracted Topics:
- delivery partner rude
- food quality issue

This confirms accurate semantic understanding.

### 2. Keyword Independence Test
Synthetic reviews were introduced without using explicit keywords.

Example:
"The rider behaved unprofessionally and was disrespectful."

Despite the absence of keywords like "rude", the AI correctly inferred:
- delivery partner rude

This demonstrates true semantic reasoning rather than keyword matching.

### 3. Temporal Consistency Check
Topic frequencies were validated across multiple days to ensure:
- Daily batch processing is correct
- No topic leakage across dates
- Accurate rolling T-30 to T trend generation

### 4. Failure Handling
Reviews with no actionable issues correctly return empty topic lists,
ensuring noise-free trend analysis.

These validation steps ensure high recall, semantic consistency,
and robustness of the AI-driven trend analysis system.

## How to Run
```bash
python fetch_reviews.py
python llm_topic_extractor.py
python build_trend_table.py
