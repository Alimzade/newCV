from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/process_snapshot', methods=['POST'])
def process_snapshot():
    data = request.get_json()
    skills = data['skills']
    projects = data['projects']
    values = data['values']

    # Process the input text with spaCy (basic NLP processing)
    skills_summary = summarize_text(skills)
    projects_summary = summarize_text(projects)
    values_summary = summarize_text(values)

    # Return the processed snapshot
    return jsonify({
        "skills": skills_summary,
        "projects": projects_summary,
        "values": values_summary
    })

def summarize_text(text):
    doc = nlp(text)
    # Simple summarization: extracting noun chunks or key sentences
    summary = " ".join([chunk.text for chunk in doc.noun_chunks])
    return summary if summary else text

if __name__ == '__main__':
    app.run(debug=True)
