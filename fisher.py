from flask import Flask,make_response
from help import is_isbn_or_key
__author__='橘子'

app=Flask(__name__)
app.config.from_object('config')

"""
    q:普通关键字 isbn
    page
"""
@app.route('/book/search/<q>/<page>')
def search(q,page):

    isbn_or_key=is_isbn_or_key(q)


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUGE'],port=81)
