from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Jovian Careers</h1>
    <p>Welcome to the careers portal!</p>
    <p>You can now build whatever you want here.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)