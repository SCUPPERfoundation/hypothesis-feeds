from flask import render_template
from flask import request
from feedparser import parse

from . import app
from .models.alpha import ReviewDoc

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blobs = ReviewDoc.query.paginate(page)
    return render_template('home.html', blobs=blobs)
