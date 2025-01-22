from flask import Flask, jsonify
from extensions import db
from sqlalchemy import create_engine, text
from pymongo import MongoClient
from models import User, UserSpending

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

mongo_client = MongoClient("mongodb+srv://admin:admin@cluster0.vjyox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["users_vouchers"]
mongo_collection = mongo_db["vouchers"]



@app.route('/total_spent/<int:user_id>', methods=['GET'])
def total_spent(user_id):
    user_spending = db.session.query(UserSpending).filter_by(user_id=user_id).all()

    total_spending = sum(spending.money_spent for spending in user_spending)

    if total_spending > 1000:
        user_data = {
            'user_id': user_id,
            'total_spending': total_spending
        }

        mongo_collection.update_one(
            {'user_id': user_id},
            {'$set': user_data},
            upsert=True
        )

    return jsonify({
        'user_id': user_id,
        'total_spending': total_spending
    })

# @app.route('/average_spending_by_age', methods=['GET'])
# def average_spending_by_age():
#     age_ranges = {
#         "18-24": (18, 24),
#         "25-30": (25, 30),
#         "31-36": (31, 36),
#         "37-47": (37, 47),
#         ">47": (48, 100)
#     }

    averages = {}


# def send_telegram_message(message):


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)