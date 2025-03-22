#new code from here

from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle
import os
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure static assets
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/main.scss', filters='scss', output='css/main.css')
assets.register('scss_all', scss)

# Define routes
@app.route('/debug-logo')
def debug_logo():
    import os
    logo_path = os.path.join(app.static_folder, 'images', 'logo.png')
    exists = os.path.exists(logo_path)
    file_info = {}
    if exists:
        file_info = {
            'size': os.path.getsize(logo_path),
            'permissions': oct(os.stat(logo_path).st_mode)[-3:],
            'path': logo_path,
            'static_url': app.static_url_path
        }
    return jsonify({
        'file_exists': exists,
        'static_folder': app.static_folder,
        'file_info': file_info
    })

@app.route('/')
def index():
    # Sample project data - this would be replaced by a database in a production app
    projects = [
        {
            "id": "1",
            "title": "AI Data Pipeline",
            "description": "End-to-end data pipeline for ML models with automated cleaning and preprocessing",
            "image": "/static/images/projects/Designer_1.jpeg",
            "tags": ["Python", "Apache Airflow", "TensorFlow", "AWS"],
            "category": "Machine Learning"
        },
        {
            "id": "2",
            "title": "NLP Sentiment Analysis",
            "description": "Real-time sentiment analysis tool for social media data",
            "image": "/static/images/projects/Designer_1.jpeg",
            "tags": ["Python", "NLTK", "Transformers", "React"],
            "category": "Machine Learning"
        },
        {
            "id": "3",
            "title": "Portfolio Website",
            "description": "Responsive portfolio website built with Flask and modern design principles",
            "image": "/static/images/projects/Designer_1.jpeg",
            "tags": ["Python", "Flask", "Jinja2", "TailwindCSS"],
            "category": "Web Development"
        }
    ]
    
    # Skills data
    skill_categories = [
        {
            "title": "Data Engineering",
            "icon": "gear",
            "skills": [
                {"name": "Apache Spark", "icon": "apache"},                
                {"name": "SQL", "icon": "postgresql"},
                {"name": "Airflow", "icon": "airflow"},
                {"name": "Python", "icon": "Python"}
            ]
        },
        {
            "title": "Databases",
            "icon": "database",
            "skills": [
                {"name": "Oracle", "icon": "Oracle"},
                {"name": "MySQL", "icon": "MySQL"},
                {"name": "SQL Server", "icon": "SQL Server"},
                {"name": "Azure SQL Database", "icon": "Azure SQL Database"}
            ]
        },
        {
            "title": "Data Platforms",
            "icon": "code",
            "skills": [
                {"name": "Databricks", "icon": "Databricks"},
                {"name": "Snowflake", "icon": "Snowflake"},
                {"name": "Palantir", "icon": "Palantir"},
                {"name": "AzureML", "icon": "AzureML"}
            ]
        }
    ]
    
    # Contact info
    contact_info = {
        "email": "contact@example.com",
        "location": "San Francisco, CA",
        "social": {
            "github": "https://github.com/yourusername",
            "linkedin": "https://linkedin.com/in/yourusername",
            "twitter": "https://twitter.com/yourusername"
        }
    }
    
    return render_template('index.html', 
                           projects=projects, 
                           skill_categories=skill_categories,
                           contact_info=contact_info,
                           now=datetime.datetime.now())

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # In a production app, you would send an email or store this in a database
    print(f"Contact form submission: {data}")
    # Simple validation
    if not all(key in data for key in ['name', 'email', 'subject', 'message']):
        return jsonify({"success": False, "message": "Missing required fields"}), 400
    
    # For demo purposes, just return success
    return jsonify({"success": True, "message": "Message sent successfully!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)