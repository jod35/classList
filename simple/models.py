from . import db

class Student(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(),nullable=False)
    age=db.Column(db.Integer(),nullable=False)
    grade=db.Column(db.Integer(),nullable=False)

    def __repr__(self):
        return f"student {self.id}"