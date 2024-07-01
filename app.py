from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Проект 15",
        "description": "Краткое описание проекта 1",
        "date": "Январь 2022 - Март 2022",
        "tools": "HTML, CSS, JavaScript, React",
        "role": "Разработчик интерфейса",
    },
    {
        "name": "Проект 2",
        "description": "Краткое описание проекта 2",
        "date": "Июнь 2021 - Август 2021",
        "tools": "Python, Django",
        "role": "Полный стек разработчик",
    }
]

@app.route('/')
def home():
    # return 'Hello world!'
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='4999')
