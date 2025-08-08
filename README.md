# Candidate Recommendation Engine

A simple Streamlit web app that recommends the best candidates for a job based on their resume content.

## 🔍 Features
- Upload multiple resumes (PDF/DOCX)
- Paste job description
- Ranks top 5–10 candidates using cosine similarity
- BONUS: Summarizes why the candidate is a good fit (OpenAI)

## How to Use
1. Paste a job description
2. Upload one or more resumes
3. Click "Find Best Candidates"
4. See top matches and scores

## Stack
- Streamlit (UI)
- Sentence Transformers (Embeddings)
- scikit-learn (Similarity)
- OpenAI (Summarization)

## Deployment
[Link to deployed app](https://candidate-recommender-aakanksha.streamlit.app/)

## Note
If OpenAI summary isn't working, it may be due to API quota limits.
