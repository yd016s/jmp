from blog import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(120), unique=True, nullable=False)
    html=db.Column(db.String(200), unique=True)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'Post("{self.id}", "{self.title}", "{self.html}", "{self.date_posted}")' 
