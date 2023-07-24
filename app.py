from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    
    # return "<p>Hello, World!</p>"

@app.route("/")
def sign():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)