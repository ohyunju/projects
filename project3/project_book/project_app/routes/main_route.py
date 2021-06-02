from flask import Blueprint, render_template, request
from project_app.utils import main_funcs
from project_app.models.bestsell_model import add_bestsells, get_bestsells
from project_app.models.bookmylist_model import get_mylists, get_mylist
from project_app.models.comparelist_model import get_comparelists, get_comparelist
import os
import csv

bp = Blueprint('main', __name__)

yes24_FILEPATH = os.path.join(os.getcwd(), 'project_app', 'yes24.csv')
kyobo_FILEPATH = os.path.join(os.getcwd(), 'project_app', 'kyobo.csv')
aladdin_FILEPATH = os.path.join(os.getcwd(), 'project_app', 'aladdin.csv')

@bp.route('/')
def index():
    
    raw_sell=[]
    with open(yes24_FILEPATH, 'r', encoding='utf-8') as yes24:
      yes24_reader = csv.DictReader(yes24)

      for cols in yes24_reader:
        raw_sell.append(cols)
    add_bestsells(raw_sell,which='yes24')

    raw_sell=[]
    with open(kyobo_FILEPATH, 'r', encoding='utf-8') as kyobo:
      kyobo_reader = csv.DictReader(kyobo)
      
      for cols in kyobo_reader:
        raw_sell.append(cols)
    add_bestsells(raw_sell,which='kyobo')

    raw_sell=[]
    with open(aladdin_FILEPATH, 'r', encoding='utf-8') as aladdin:
      aladdin_reader = csv.DictReader(aladdin)
      
      for cols in aladdin_reader:
        raw_sell.append(cols)
    add_bestsells(raw_sell,which='aladdin')

    yes24_bestsell_list=get_bestsells('yes24')
    kyobo_bestsell_list=get_bestsells('kyobo')
    aladdin_bestsell_list=get_bestsells('aladdin')

    return render_template('index.html',yes24_bestsell_list=yes24_bestsell_list,\
        kyobo_bestsell_list=kyobo_bestsell_list,aladdin_bestsell_list=aladdin_bestsell_list)

@bp.route('/compare', methods=["GET", "POST"])
def compare_index():
    
    bookMylist=get_mylists()
    
    mylist_isbn=None
    result_list=[]
    if request.method == "POST":
        mylist_isbn = request.form.get("mylist", None)
        mylist = get_mylist(mylist_isbn)
        compare_lists=get_comparelists()
        result = main_funcs.predict_book(compare_lists=compare_lists, mylist=mylist)
        result_list = get_comparelist(result)
        print(result_list)
    return render_template('recommend.html',bookMylist=bookMylist,result_list=result_list,mylist_isbn=mylist_isbn)

@bp.route('/book', methods=["GET", "POST"])
def user_index():
    return render_template('book.html')

@bp.route('/list')
def list_index():
    bookMylist=get_mylists()
    return render_template('list.html',bookMylist=bookMylist)