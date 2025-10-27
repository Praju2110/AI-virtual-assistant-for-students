# In config.py

import os
from dotenv import load_dotenv

# This line finds the .env file in your project root and loads its variables
# into the environment, making them accessible to os.getenv()
load_dotenv()

# This line now successfully reads the loaded variable and stores it
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")