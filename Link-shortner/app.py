from flask import Flask, render_template, request, redirect
import string
import random
import sqlite3

app = Flask(__name__)

# Create a connection to SQLite database with check_same_thread=False
conn = sqlite3.connect('urls.db', check_same_thread=False)
c = conn.cursor()

# Create a table to store URLs
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_url TEXT)''')
conn.commit()

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))  # 6-character short URL
    return short_url

# Home page with a form to submit URLs
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    
    # Check if the URL already exists in the database
    c.execute("SELECT short_url FROM urls WHERE original_url=?", (original_url,))
    row = c.fetchone()
    if row:
        short_url = row[0]
    else:
        short_url = generate_short_url()
        c.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
        conn.commit()
    
    return render_template('shortened.html', original_url=original_url, short_url=short_url)

# Route to redirect to original URL
@app.route('/<short_url>')
def redirect_to_url(short_url):
    c.execute("SELECT original_url FROM urls WHERE short_url=?", (short_url,))
    row = c.fetchone()
    if row:
        original_url = row[0]
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
