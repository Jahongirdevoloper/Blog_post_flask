from root import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pic = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return self.title

    def __init__(self, _id: int = None,
                 title: str = None,
                 body: str = None,
                 pic: str = None,
                 created_by: int = None,
                 created_at: int = None):
        self.id = _id
        self.title = title
        self.pic = pic
        self.body = body
        self.created_by = created_by
        self.created_at = created_at

    def __call__(self, *args, **kwargs):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
