from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Доброго ранку"
    elif 12 <= hour < 18:
        greeting = "Добрий день"
    else:
        greeting = "Добрий вечір"

    tasks = [
        "Перше завдання",
        "Друге завдання",
        "Третє завдання",
        "Четверте завдання"
    ]
    return render_template('index.html', greeting=greeting, tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
