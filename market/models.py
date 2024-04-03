from market import db 

class Item(db.Model):
    ib = db.Column(db.Integer() , primary_key=True )
    name = db.Column(db.String(length=30), nullable=False , unique=True) # we can limit character counts # we don't want null fields
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12) , nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f"Item {self.name}"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Item {self.name}"


