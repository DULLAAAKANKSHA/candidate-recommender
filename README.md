# Candidate Recommendation Engine

A Streamlit web app that recommends the best candidates for a job based on their resumes and job description.

## 🔍 Features
- Upload multiple resumes in PDF or DOCX format  
- Input a job description as text  
- Ranks the top 5–10 candidates by cosine similarity of text embeddings  
- BONUS: AI-generated summary explaining why the candidate is a good fit (using OpenAI API)  

## How to Use
1. Paste the job description into the text box  
2. Upload one or more resumes (PDF or DOCX)  
3. Click **Find Best Candidates**  
4. View the ranked list of top matching candidates with similarity scores and summaries  

## Tech Stack
- Streamlit — user interface and app hosting  
- Sentence Transformers — generating text embeddings  
- scikit-learn — calculating cosine similarity  
- OpenAI API — generating candidate fit summaries  

## Approach
1. **Input Handling:** Accepts job description as text input and resumes as uploaded files or text.  
2. **Text Extraction:** Extracts raw text from uploaded resumes (handles PDF and DOCX formats).  
3. **Embedding Generation:** Converts both job description and resumes into fixed-size vector embeddings using Sentence Transformers.  
4. **Similarity Calculation:** Computes cosine similarity between job description embedding and each resume embedding to rank candidates.  
5. **Summary Generation:** Optionally uses OpenAI’s API to generate a short summary explaining why the candidate matches the role well.  

## Code Structure
- `app.py`: Main Streamlit app file handling UI and workflow    
- `requirements.txt`: Python dependencies required to run the app  

## Deployment
[Live app on Streamlit](https://candidate-recommender-aakanksha.streamlit.app/)

## Assumptions and Notes
- Resumes must be in PDF or DOCX format and contain extractable text  
- OpenAI API key is required and must be set as an environment variable for summaries to work  
- API quota limits might affect the summary generation feature  

