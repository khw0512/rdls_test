from flask import Flask , render_template
app = Flask(__name__)

@app.route('/hellodeepblue')
def hello_world():
    return render_template('index.html')

@app.route('/hello')
def hello_home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=8000)