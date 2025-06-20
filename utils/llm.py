from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Summarize this scientific paper:\n{text}"}]
    )
    return response.choices[0].message.content.strip()

def generate_review(text, tone="Neutral"):
    prompt = f"""You are a scientific peer reviewer. Write a {tone.lower()} tone review for this manuscript:\n{text}"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def analyze_citations(text):
    prompt = "Extract the references section and analyze the citations: publication year, diversity, recency, and relevance.\n\n" + text
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
