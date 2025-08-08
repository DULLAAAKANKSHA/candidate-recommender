import streamlit as st
import fitz  # PyMuPDF for PDF reading
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI  # updated import

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # new client initialization

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract text from resume file
def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        pdf_file = fitz.open(stream=file.read(), filetype="pdf")
        for page in pdf_file:
            text += page.get_text()
        return text
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""

# Convert text to embedding
def get_embedding(text):
    return model.encode(text)

# Compute similarity
def compute_similarity(job_emb, resume_embs):
    return cosine_similarity([job_emb], resume_embs)[0]

# Generate AI summary — UPDATED for new OpenAI client API
def summarize_fit(job_desc, resume_text):
    prompt = f"""Job Description:
{job_desc}

Candidate Resume:
{resume_text[:2000]}  # Trimmed for token limit

In 2–3 lines, explain why this candidate is a good fit for the job:"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Summary unavailable. Error: {e}"

# Streamlit UI
st.title("🧠 Candidate Recommendation Engine")

job_description = st.text_area("📄 Paste the Job Description")

uploaded_files = st.file_uploader(
    "📂 Upload Resumes (PDF or DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if st.button("Find Best Candidates"):
    if job_description and uploaded_files:
        job_embedding = get_embedding(job_description)
        results = []

        for file in uploaded_files:
            resume_text = extract_text(file)
            if resume_text:
                emb = get_embedding(resume_text)
                sim = compute_similarity(job_embedding, [emb])[0]
                summary = summarize_fit(job_description, resume_text)

                results.append({
                    "Candidate Name": file.name,
                    "Similarity Score": round(sim, 3),
                    "AI Summary": summary
                })

        df = pd.DataFrame(
            sorted(results, key=lambda x: x["Similarity Score"], reverse=True)
        )
        st.subheader("📋 Top Matching Candidates")
        st.dataframe(df.head(10))
    else:
        st.warning("⚠️ Please enter a job description and upload at least one resume.")