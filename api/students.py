import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load data from q-vercel-python.json
with open('api/q-vercel-python.json', 'r') as f: 
    student_marks = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get names from query parameters
    names = request.args.getlist('name')
    
    # Fetch marks for requested names
    marks = [student_marks.get(name, None) for name in names]
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
