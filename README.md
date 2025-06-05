Portfolio Website Project
A professional portfolio website with a responsive design built using HTML, CSS, and JavaScript for the frontend, with a Python/Flask backend for handling contact form submissions and storing them in an SQLite database.

Features
Modern, responsive design that looks great on all devices
Smooth scrolling navigation
Animated sections and elements
Contact form with data stored in SQLite database
Professional project showcase with filtering
Skills section highlighting developer capabilities
Clean and maintainable code structure
Project Structure
portfolio-website/
├── index.html         # Main HTML file
├── styles.css         # CSS styles
├── script.js          # Frontend JavaScript
├── app.py             # Python/Flask backend
├── portfolio.db       # SQLite database (created when app runs)
└── README.md          # This file
Frontend Technologies
HTML5
CSS3 (with animations and transitions)
JavaScript (ES6+)
Font Awesome (for icons)
Backend Technologies
Python 3.x
Flask (web framework)
SQLite (database)
Setup and Installation
Clone the repository
bash
git clone https://github.com/yourusername/portfolio-website.git
cd portfolio-website
Set up a Python virtual environment (recommended)
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies
bash
pip install flask
Run the application
bash
python app.py
Open your browser and navigate to http://localhost:5000
Database Schema
The contact information is stored in an SQLite database with the following schema:

sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Customization
To customize this portfolio for your own use:

Update the personal information and content in index.html
Replace placeholder images with your own
Update project information with your own projects
Modify skills and experience sections
Customize colors and styling in styles.css
Deployment
To deploy this application:

Set up a server with Python installed
Install Flask on the server
Set the appropriate environment variables for production
Use a production WSGI server like Gunicorn
Configure a reverse proxy like Nginx to serve the static files
Example deployment setup with Gunicorn and Nginx:

bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 127.0.0.1:8000 app:app
Configure Nginx to proxy requests to Gunicorn and serve static files directly.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Background image from Unsplash
Font Awesome for icons
Google Fonts for typography
