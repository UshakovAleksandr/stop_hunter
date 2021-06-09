from api import db


class ClientModel(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=False)
    surname = db.Column(db.String(32), unique=False)
    email = db.Column(db.String(120), unique=True)
    terrorist = db.Column(db.Boolean(), default=False, nullable=False)
    criminal_record = db.Column(db.Boolean(), default=False, nullable=False)
    mental_health = db.Column(db.Boolean(), default=False, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            "surname": self.surname,
            "email": self.email,
            "terrorist": self.terrorist,
            "criminal_record": self.criminal_record,
            "mental_health": self.mental_health
        }
