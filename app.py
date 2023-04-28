from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('badpage.html')

@app.route('/lottery')
def lotter():
    return render_template('lotter.html')

if __name__ == '__main__':
    app.run(debug=True)