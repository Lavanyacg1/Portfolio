from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from datetime import datetime

# Create Flask application
app = Flask(__name__, static_folder='.', static_url_path='')

# Database setup
def init_db():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    
    # Create contacts table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        subject TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route for the home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# API endpoint for contact form
@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'success': False, 'message': f'Missing required field: {field}'}), 400
        
        # Basic email validation
        if '@' not in data['email'] or '.' not in data['email']:
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        # Connect to database
        conn = sqlite3.connect('portfolio.db')
        cursor = conn.cursor()
        
        # Insert contact message into database
        cursor.execute(
            'INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)',
            (data['name'], data['email'], data['subject'], data['message'])
        )
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        # Return success response
        return jsonify({'success': True, 'message': 'Contact message saved successfully'})
    
    except Exception as e:
        # Log the error (in a production app, you'd use proper logging)
        print(f"Error processing contact form: {str(e)}")
        return jsonify({'success': False, 'message': 'Server error. Please try again later.'}), 500

# API endpoint to get all contacts (admin only - would need authentication in production)
@app.route('/api/admin/contacts', methods=['GET'])
def get_contacts():
    try:
        # In a real app, you would check authentication here
        # This is just for demonstration purposes
        
        # Connect to database
        conn = sqlite3.connect('portfolio.db')
        conn.row_factory = sqlite3.Row  # This enables name-based access to columns
        cursor = conn.cursor()
        
        # Get all contacts
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = [dict(row) for row in cursor.fetchall()]
        
        # Close connection
        conn.close()
        
        # Return contacts as JSON
        return jsonify({'success': True, 'contacts': contacts})
    
    except Exception as e:
        print(f"Error retrieving contacts: {str(e)}")
        return jsonify({'success': False, 'message': 'Server error. Please try again later.'}), 500

# Run the application
if __name__ == '__main__':
    # In development, use debug mode
    app.run(debug=True)
    
    # In production, you would use:
    # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))