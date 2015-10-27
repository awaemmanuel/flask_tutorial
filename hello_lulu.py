from flask import Flask,render_template
app = Flask(__name__)

@app.route('/hello_lulu2')
def hello_world_lulu():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
    