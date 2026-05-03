from flask import Flask, flash, jsonify, redirect,render_template, url_for, request
import json
from dotenv import load_dotenv
import os
import pymongo


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['thoughts']

app = Flask(__name__)
app.secret_key = "whatsonyourmind"  # Required for flashing

# Route to read and return JSON data
@app.route('/api')
def get_json_data():
    try:
        # Open and load the local JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        # Return the data as a JSON list/response
        return jsonify(data)
    
    except FileNotFoundError:
        return jsonify({"error": "JSON file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in file"}), 500
    
#default route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission or any POST request logic here
        data = {"name": request.form.get("thought")}

        try:
        
            # Insert data into MongoDB
            collection.insert_one(data)
            return redirect(url_for('success'))
        except Exception as e:
            # If insertion fails, stay on same page and show error
            flash(f"Something went wrong, error details: {str(e)}", "error")
            return render_template('index.html') # Render the form again with error message
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/thoughts')
def thoughts():
    try:
        # Fetch all thoughts from MongoDB
        thoughts = list(collection.find({}, {'_id': 0}))  # Exclude the MongoDB ID field
        return jsonify(thoughts)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch thoughts, error details: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)