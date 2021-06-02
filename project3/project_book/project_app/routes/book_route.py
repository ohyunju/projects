from flask import Blueprint, request, redirect, url_for, Response
from project_app.services import naver_api
from project_app.models import comparelist_model, bookmylist_model
from project_app.models.comparelist_model import Comparelist
from project_app.models.bookmylist_model import get_mylists, BookMylist
from flask import render_template

bp = Blueprint('book', __name__)

@bp.route('/book', methods=["GET", "POST"])
def search_book():
    
    query = request.form.get('query', default = None)
    book_list = None

    if not query:
      alert_msg="검색할 값을 입력해주세요"
      return render_template('book.html', book_list=book_list, query=query, alert_msg=alert_msg)

    if request.method == "POST":
      book_list = naver_api.get_books(query=query,display=100)
      comparelist_model.add_comparelist(book_list=book_list)
      return render_template('book.html', book_list=book_list, query=query)

    return render_template('book.html', book_list=book_list, query=query)

@bp.route('/bookadd/')
@bp.route('/bookadd/<isbn>',methods=["GET"])
def add_mylist(isbn=None):

    query = request.args.get('query', default = None)
    book_list = naver_api.get_books(query=query,display=20)

    if isbn is None :
      return "", 400
    
    compare_book =  Comparelist.query.filter(Comparelist.isbn==isbn).first()
    if not compare_book:
      return "", 404
    
    bookmylist_model.add_mylist(compare_book=compare_book)
    return render_template('book.html', book_list=book_list, query=query)

@bp.route('/bookdel/')
@bp.route('/bookdel/<isbn>',methods=["GET"])
def del_mylist(isbn=None):

    if isbn is None :
      return "", 400
    
    del_book =  BookMylist.query.filter(Comparelist.isbn==isbn).first()
    if not del_book:
      return "", 404
    
    bookmylist_model.del_mylist(isbn=isbn)
    bookMylist=get_mylists()

    return render_template('list.html', bookMylist=bookMylist)
