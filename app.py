from flask import Flask, render_template
from projects import projects

app = Flask(__name__)



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
