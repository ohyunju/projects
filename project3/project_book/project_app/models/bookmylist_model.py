from project_app import db

class BookMylist(db.Model):
    __tablename__ = 'bookmylist'

    title = db.Column(db.String(256), nullable=False)
    link = db.Column(db.String(256))
    image = db.Column(db.String(256))
    author = db.Column(db.String(256))
    price =  db.Column(db.String(256))
    discount = db.Column(db.String(256))
    publisher = db.Column(db.String(256))
    isbn =  db.Column(db.String(256),primary_key=True)
    description = db.Column(db.Text)
    pubdate = db.Column(db.String(256))

    def __repr__(self):
        return f"User {self.isbn}"

def add_mylist(compare_book):
    
    title = compare_book.title
    link = compare_book.link
    image = compare_book.image
    author = compare_book.author
    price =  compare_book.price
    discount = compare_book.discount
    publisher = compare_book.publisher
    isbn =  compare_book.isbn
    description = compare_book.description
    pubdate = compare_book.pubdate

    if BookMylist.query.filter(BookMylist.isbn == isbn).first() == None :
        updated = BookMylist(title=title, link=link, image=image, author=author,\
            price=price, discount=discount, publisher=publisher, isbn=isbn,\
            description=description, pubdate=pubdate)
        db.session.add(updated)
        db.session.commit() 
    
def get_mylists() :
    return BookMylist.query.all()

def del_mylist(isbn):
    mylist = BookMylist.query.filter(BookMylist.isbn == isbn).first()
    db.session.delete(mylist)
    db.session.commit()
    
def get_mylist(isbn):
    return BookMylist.query.filter(BookMylist.isbn == isbn).first()