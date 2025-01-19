# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample gift database with categories and similar gifts
GIFTS = {
    'tech': [
        {'name': 'Wireless Earbuds', 'similar': ['Bluetooth Speaker', 'Noise-Cancelling Headphones']},
        {'name': 'Smart Watch', 'similar': ['Fitness Tracker', 'Digital Watch']},
        {'name': 'Portable Power Bank', 'similar': ['Wireless Charger', 'USB Hub']}
    ],
    'lifestyle': [
        {'name': 'Scented Candle Set', 'similar': ['Essential Oil Diffuser', 'Reed Diffuser']},
        {'name': 'Yoga Mat', 'similar': ['Resistance Bands', 'Meditation Cushion']},
        {'name': 'Coffee Machine', 'similar': ['Tea Set', 'French Press']}
    ],
    'hobby': [
        {'name': 'Digital Drawing Tablet', 'similar': ['Art Supply Set', 'Sketchbook Set']},
        {'name': 'Board Game Collection', 'similar': ['Puzzle Set', 'Card Game Set']},
        {'name': 'Plant Growing Kit', 'similar': ['Succulent Set', 'Herb Garden Kit']}
    ]
}

# Questions to determine gift preferences
QUESTIONS = [
    "Does the recipient like technology?",
    "Do they enjoy outdoor activities?",
    "Are they interested in cooking?",
    "Do they work from home?",
    "Are they into fitness?",
    "Do they enjoy reading?",
    "Are they music lovers?",
    "Do they like gaming?",
    "Are they interested in art?",
    "Do they enjoy DIY projects?",
    "Are they pet owners?",
    "Do they like photography?",
    "Are they coffee/tea enthusiasts?",
    "Do they enjoy meditation/yoga?",
    "Are they into gardening?",
    "Do they collect anything?",
    "Are they fashion-conscious?",
    "Do they enjoy traveling?",
    "Are they environmentally conscious?",
    "Do they like board games?",
    "Are they into home decoration?",
    "Do they enjoy cooking?",
    "Are they interested in wellness?",
    "Do they work in a creative field?",
    "Are they interested in smart home devices?"
]

@app.route('/')
def home():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/recommend', methods=['POST'])
def recommend():
    answers = request.json['answers']
    
    # Simple recommendation logic based on answers
    tech_score = sum(1 for i, ans in enumerate(answers) if ans and i in [0, 3, 6, 7, 24]) / 5
    lifestyle_score = sum(1 for i, ans in enumerate(answers) if ans and i in [4, 13, 16, 18, 22]) / 5
    hobby_score = sum(1 for i, ans in enumerate(answers) if ans and i in [8, 9, 14, 19, 20]) / 5
    
    # Choose category based on highest score
    scores = {'tech': tech_score, 'lifestyle': lifestyle_score, 'hobby': hobby_score}
    chosen_category = max(scores, key=scores.get)
    
    # Select random gift from chosen category
    recommended_gift = random.choice(GIFTS[chosen_category])
    
    return jsonify({'gift': recommended_gift['name'], 'similar': recommended_gift['similar']})

if __name__ == '__main__':
    app.run(debug=True)
