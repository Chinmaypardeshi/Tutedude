# DevOps Assignment: Flask & MongoDB Atlas Integration
**Student Name:** Chinmay Pardeshi  
**Project Folder Name:** `Flask_and_MongoDB_Chinmay_Pardeshi`  

---

## 1. Project Overview & Objectives
This project demonstrates the implementation of a full-stack Flask web application integrated with a backend JSON data store and a cloud-hosted MongoDB Atlas database. The application fulfills two primary operational tasks:
1. **Task 1 (JSON API Route):** An `/api` endpoint that reads structured application records from a local backend file (`data.json`) and returns them as a serialized JSON list response.
2. **Task 2 (Frontend Form with MongoDB Atlas):** A responsive web interface that captures user submissions, validates input parameters, securely inserts records into a MongoDB Atlas cluster, handles errors inline without redirection, and redirects to a success confirmation view upon successful insertion.

---

## 2. Environment Setup & Dependencies

### Prerequisites
* Python 3.10+ installed on Windows.
* Active internet connection for MongoDB Atlas cloud cluster communication.

### Dependencies (`requirements.txt`)
The project utilizes lightweight, production-stable Python libraries:
```text
Flask==3.1.0
pymongo==4.11.0
dnspython==2.7.0
```

### Installation Commands & Terminal Execution
To set up the local environment and install required packages, run the following commands in your terminal:

```bash
# Clone or open project directory
cd Flask_and_MongoDB_Chinmay_Pardeshi

# Install required Python dependencies
pip install -r requirements.txt

# Start the Flask development server
python app.py
```

*Terminal Screenshot Reference:*  
*(Include a screenshot here showing the successful execution of `pip install -r requirements.txt` and the Flask server starting up on `http://127.0.0.1:5000`)*

---

## 3. Task 1: JSON API Route (`/api`)

### Implementation Details
The `/api` route reads records dynamically from the backend file `data.json` located in the application root directory. If the file is successfully located and parsed, it responds with an HTTP status code `200` and a valid JSON list.

### Code Snippet (`app.py`)
```python
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
```

### Output Verification
* **Endpoint URL:** `http://127.0.0.1:5000/api`
* *Browser / API Output Screenshot Reference:*  
  *(Include a screenshot of your browser or `curl` command displaying the rendered JSON list returned by the server)*

---

## 4. Task 2: Frontend Form & MongoDB Atlas Integration

### Implementation Details
The frontend form captures user input fields (`name`, `email`, `message`) via an HTTP POST request to the `/submit` route. The Flask backend establishes a secure connection to MongoDB Atlas using `pymongo` and appends the document to the target collection (`devops_assignment_db.submissions`).

### Key Features:
* **Success Handling:** Upon successful database insertion (`insert_one`), the user is redirected via `redirect(url_for('success_page'))` to view the mandatory success message: **“Data submitted successfully”**.
* **Error Handling:** If validation fails or database connectivity drops, exceptions are caught locally, re-rendering `index.html` with an inline error banner **without page redirection**.

### Code Snippet (`app.py` Submission Route)
```python
@app.route('/submit', methods=['POST'])
def handle_form_submission():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not message:
        return render_template('index.html', error="All fields are mandatory. Please fill in all inputs.")

    document = {
        "name": name,
        "email": email,
        "message": message
    }

    try:
        collection.insert_one(document)
        return redirect(url_for('success_page'))
    except Exception as e:
        error_msg = f"Database insertion failed: {str(e)}"
        return render_template('index.html', error=error_msg)
```

---

## 5. Visual Proof of Execution & Screenshots

### A. Frontend Form Interface
* *Screenshot Reference:*  
  *(Include a screenshot of the form loaded in your browser at `http://127.0.0.1:5000`)*

### B. Successful Data Submission & Redirection
* *Screenshot Reference:*  
  *(Include a screenshot of the success page displaying the text: **“Data submitted successfully”**)*

### C. MongoDB Atlas Database Verification
* *Screenshot Reference:*  
  *(Include a screenshot of your MongoDB Atlas **Data Explorer** showing the newly stored document inside `devops_assignment_db.submissions`)*

### D. Error Handling (Inline Reporting)
* *Screenshot Reference:*  
  *(Include a screenshot showing the error alert banner displayed on the same form page when submitting incomplete or invalid data)*

---

## 6. GitHub Repository Link
* **Public GitHub Repository URL:** [https://github.com/ChinmayPardeshi/Flask_and_MongoDB_Assignment](https://github.com/ChinmayPardeshi/Flask_and_MongoDB_Assignment) *(Replace with your actual public repository link)*