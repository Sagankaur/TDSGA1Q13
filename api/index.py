from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the JSON data
with open('q-vercel-python.json', 'r') as f:
    students_data = json.load(f)

# Convert the list of dictionaries to a dictionary for faster lookup
students_dict = {list(student.keys())[0]: list(student.values())[0] for student in students_data}

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    if not name:
        return {"error": "No names provided"}
    
    marks = [students_dict.get(n, None) for n in name]
    return {"marks": marks}

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

