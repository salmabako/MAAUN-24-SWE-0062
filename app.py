from flask import Flask, render_template, request, redirect, url_for
from models import Business, Directory

app = Flask(__name__)

kubwa_hub = Directory()

@app.route('/')
def home():
    """Route 1: Displays the Stack of recently added businesses."""
    recent_businesses = kubwa_hub.get_recent_businesses()
    return render_template('index.html', businesses=recent_businesses)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
