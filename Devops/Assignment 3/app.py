import os
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

app = Flask(__name__)

# Task 1: File-backed JSON API Route configuration
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

# Task 2: MongoDB Atlas Configuration
# Replace with your secure MongoDB Atlas connection string and database name
MONGO_URI = "mongodb+srv://chinmayvpardeshi_db_user:chinmay@tutedude.xejh12o.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "devops_assignment_db"
COLLECTION_NAME = "submissions"

try:
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = mongo_client[DB_NAME]
    collection = db[COLLECTION_NAME]
except Exception as e:
    print(f"Warning: MongoDB connection initialization failed: {e}")

@app.route('/')
def index():
    """Renders the frontend form."""
    return render_template('index.html', error=None)

@app.route('/api', methods=['GET'])
def get_api_data():
    """
    Task 1: /api route that reads data from a backend file (data.json) 
    and returns it as a JSON list response.
    """
    try:
        if not os.path.exists(DATA_FILE_PATH):
            return jsonify({"error": "Backend data file not found."}), 404
        
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submit', methods=['POST'])
def handle_form_submission():
    """
    Task 2: Frontend form submission handler.
    Inserts data into MongoDB Atlas. Redirects on success or 
    renders the form with an error message on failure.
    """
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    # Basic server-side validation
    if not name or not email or not message:
        return render_template('index.html', error="All fields are mandatory. Please fill in all inputs.")

    document = {
        "name": name,
        "email": email,
        "message": message
    }

    try:
        # Insert document into MongoDB Atlas collection
        collection.insert_one(document)
        return redirect(url_for('success_page'))
    except Exception as e:
        error_msg = f"Database insertion failed: {str(e)}"
        return render_template('index.html', error=error_msg)

@app.route('/success')
def success_page():
    """Renders the success confirmation page."""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)