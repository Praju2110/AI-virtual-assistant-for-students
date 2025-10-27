# In start.py

from dotenv import load_dotenv

# Load environment variables. This MUST be the first thing your app does.
load_dotenv()

# Now, import and run your app
import uvicorn
from app import app # Assuming your Flask app instance is named 'app' in 'app.py'

if __name__ == "__main__":
    print("Starting application with uvicorn...")
    # Your uvicorn.run command here
    uvicorn.run(app, host="0.0.0.0", port=8000) # Or however you run it