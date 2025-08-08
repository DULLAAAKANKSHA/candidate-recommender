from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    # List available models
    models = client.models.list()
    print("✅ Success! Available models:")
    for model in models.data[:5]:  # Show first 5 models
        print("-", model.id)
except Exception as e:
    print("❌ Failed:", e)
