from project_app import db
from project_app.services.embedding_api import get_embeddings

class Comparelist(db.Model):
    __tablename__ = 'comparelist'

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
    embedding = db.Column(db.PickleType)

    def __repr__(self):
        return f"User {self.isbn}"

def add_comparelist(book_list):
    
    for i in range(0,len(book_list)):
        description_list=[book_list[i]['title']+book_list[i]['author']+book_list[i]['description']]
        
        title = book_list[i]['title']
        link = book_list[i]['link']
        image = book_list[i]['image']
        author = book_list[i]['author']
        price =  book_list[i]['price']
        discount = book_list[i]['discount']
        publisher = book_list[i]['publisher']
        isbn =  book_list[i]['isbn']
        description = book_list[i]['description']
        pubdate = book_list[i]['pubdate']
        embedding = get_embeddings(description_list)[0]
        
        if Comparelist.query.filter(Comparelist.isbn == isbn).first() == None :
            updated = Comparelist(title=title, link=link, image=image, author=author,\
                price=price, discount=discount, publisher=publisher, isbn=isbn,\
                description=description, pubdate=pubdate, embedding=embedding)
            db.session.add(updated)
            db.session.commit()

def get_comparelists():
    return Comparelist.query.all()

def get_comparelist(isbn):
    return Comparelist.query.filter(Comparelist.isbn == isbn).first()
