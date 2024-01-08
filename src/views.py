from flask import Blueprint, render_template, redirect, url_for ,g, request
import json
from urllib.request import urlopen
from urllib.parse import quote


bp = Blueprint('views', __name__)

API_KEY = 'AIzaSyBPEX1Y6p-PBQU6IWHGjkEuR0xikDQtgZI'
api = 'https://www.googleapis.com/books/v1/volumes?q=search+terms'

@bp.route('/')
def index():
    if g.user:
        return render_template('content/index.html')
    else:
        return render_template('content/home.html')
    
@bp.route('/your_list')
def your_list():
    return render_template('content/your_list.html')
