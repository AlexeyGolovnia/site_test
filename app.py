from flask import Flask, render_template

app = Flask(__name__)

projects = [
    
    {
        "name": "Information Dashboards",
        "description": "\
    I developed comprehensive information dashboards tailored for executive management.\
    These dashboards provided a real-time overview of key production metrics, empowering leadership to monitor performance indicators and swiftly respond to any fluctuations or emerging issues.\
    This initiative significantly improved decision-making processes and operational efficiency by ensuring that critical data was always accessible and actionable.",
        "date": "Январь 2022,Март 2022",
        "tools": "- Python,- Jupyter notebook,- Apache Airflow,- SQLAlchemy,- Seaborn,- Matplotlib",
        # "role": "Разработчик интерфейса",
    },

    {
        "name": "Проект 2",
        "description": "Краткое описание проекта 2",
        "date": "Июнь 2021,Август 2021",
        "tools": "Python, Django",
        # "role": "Полный стек разработчик",
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
