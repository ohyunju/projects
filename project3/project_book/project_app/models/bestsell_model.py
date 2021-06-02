from project_app import db

class Bestsell(db.Model):
    __tablename__ = 'bestsell'

    sell_id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    imageLink = db.Column(db.String(128))
    which = db.Column(db.String(32))
    
    def __repr__(self):
        return f"User {self.sell_id}"

def add_bestsells(raw_sell,which):
    
    if which=='yes24':
        for i in range(0,len(raw_sell)):
            new_sell = Bestsell(
                sell_id = i,
                title = raw_sell[i]['title'],
                author = raw_sell[i]['author'],
                imageLink = raw_sell[i]['imageLink'],
                which = which
            )
            if Bestsell.query.filter(Bestsell.sell_id == new_sell.sell_id).first() == None :
                db.session.add(new_sell)
                db.session.commit()

    if which=='kyobo':
        for i in range(0,len(raw_sell)):
            new_sell = Bestsell(
                sell_id = i+10,
                title = raw_sell[i]['title'],
                author = raw_sell[i]['author'],
                imageLink = raw_sell[i]['imageLink'],
                which = which
            )
            if Bestsell.query.filter(Bestsell.sell_id == new_sell.sell_id).first() == None :
                db.session.add(new_sell)
                db.session.commit()

    if which=='aladdin':
        for i in range(0,len(raw_sell)):
            new_sell = Bestsell(
                sell_id = i+20,
                title = raw_sell[i]['title'],
                author = raw_sell[i]['author'],
                imageLink = raw_sell[i]['imageLink'],
                which = which
            )
            if Bestsell.query.filter(Bestsell.sell_id == new_sell.sell_id).first() == None :
                db.session.add(new_sell)
                db.session.commit()

def get_bestsells(which) :
    return Bestsell.query.filter(Bestsell.which == which).all()        