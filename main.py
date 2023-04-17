from flask import Flask, send_file, jsonify, request
from faker import Faker
import requests

app = Flask(__name__)
fake = Faker()

@app.route('/')
def openPage():
    return "Hello!"

@app.errorhandler(404)
def page_not_found(error):
    return "Помилка, введіть коректну адресу!", 404


@app.route('/requrements/')
def requirements():
    return send_file('requirements.txt')
#
#
#
@app.route('/users/generate')
def generate_users():
    count = int(request.args.get('count', 100))
    users = []
    for user in range(count):
        name = fake.name()
        email = fake.email()
        users.append({'name': name, 'email': email})

    return jsonify(users)
#
#
#
@app.route('/mean/')
def get_mean():
    with open('hw.csv', 'r') as f:
        lines = f.readlines()[1:]
        heights = []
        weights = []
        for line in lines:
            parts = line.strip().split(',')
            weight = float(parts[1])
            weights.append(weight)
            height = float(parts[2])
            heights.append(height)

        mean_weight = round(sum(weights) / len(weights), 2)
        mean_height = round(sum(heights) / len(heights), 2)

        return f"Середній зріст: {mean_height} см, Середня вага: {mean_weight} кг"


@app.route('/space/')
def get_space():
    response = requests.get('http://api.open-notify.org/astros.json')
    data = response.json()

    people_on_space = data['number']

    return f"Кількість космонавтів на орбіті: {people_on_space}"



if __name__ == '__main__':
    app.run()
