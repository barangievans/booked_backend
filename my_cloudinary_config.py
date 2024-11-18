import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Correctly named dictionary with dynamic environment variable substitution
Cloudinary_config = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
}