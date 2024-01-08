from flask import Blueprint, render_template, redirect, url_for ,g, request
import json
from urllib.request import urlopen
from urllib.parse import quote


bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    if g.user:
        return render_template('content/index.html')
    else:
        return render_template('content/home.html')
    
@bp.route('/your_list')
def your_list():
    return render_template('content/your_list.html')
