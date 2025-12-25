import json
import os
from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You are an AI agent analyzing app reviews.
Extract concise issue topics from the review.
- Topics should be short (2–5 words)
- Merge similar meanings
- Ignore praise
Return output as a Python list.
"""

def extract_topics_llm(review_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": review_text}
        ],
        temperature=0.2
    )

    try:
        topics = eval(response.choices[0].message.content)
        return topics if isinstance(topics, list) else []
    except:
        return []

if __name__ == "__main__":
    if not os.path.exists("data/raw_reviews.json"):
        print("❌ Run fetch_reviews.py first")
        exit()

    with open("data/raw_reviews.json", "r", encoding="utf-8") as f:
        reviews = json.load(f)

    output = []

    for r in reviews:
        topics = extract_topics_llm(r["content"])
        for t in topics:
            output.append({
                "date": r["date"],
                "topic": t.lower()
            })

    with open("data/topic_reviews.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✅ LLM extracted {len(output)} topic instances")

