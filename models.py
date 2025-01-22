from extensions import db

class User(db.Model):
    __tablename__ = 'user_info'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

    spendings = db.relationship('UserSpending', backref='user', lazy=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }

class UserSpending(db.Model):
    __tablename__ = 'user_spending'

    spending_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'), nullable=False)
    money_spent = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='spendings')

    def to_dict(self):
        return {
            'spending_id': self.spending_id,
            'user_id': self.user_id,
            'money_spent': self.money_spent,
            'year': self.year
        }
