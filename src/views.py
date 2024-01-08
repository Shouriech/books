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
    
@bp.route('/browse', methods=['GET', 'POST'])
def browse():
    if request.method == 'POST':
        search_query = request.form.get('search')
        if search_query:  # Only proceed if search_query is not None
            # URL encode the search query and append it to the API URL
            url = api + quote(search_query) + '&key=' + API_KEY
            resp = urlopen(url)
            book_data = json.load(resp)

            volume_info = book_data['items'][0]['volumeInfo']
            author = volume_info['authors']
            author_pretty = ', '.join(author)  # Join authors into a string

            return render_template('content/browse.html', book_data=book_data, author=author_pretty)
    return render_template('content/browse.html')
