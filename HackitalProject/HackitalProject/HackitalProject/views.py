"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from HackitalProject import app

#@app.route('/')
@app.route('/home')
def home():
    """Renders the  home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/')
@app.route('/results')
def results():
    """Renders the about page."""
    return render_template(
        'results.html',
        title = 'results'
    )
