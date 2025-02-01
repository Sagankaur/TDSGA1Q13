import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load data from q-vercel-python.json
with open('q-vercel-python.json', 'r') as f:
    student_marks = json.load(f)  # Ensure this is a list of dictionaries

@app.route('/api', methods=['GET','POST'])
def get_marks():
    # Get names from query parameters
    names = request.args.getlist('name')
    
    # If no names are provided, return an empty list
    if not names:
        return jsonify({"marks": []})
    
    # Fetch marks for requested names
    marks = [student['marks'] for student in student_marks if student['name'] in names]
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
