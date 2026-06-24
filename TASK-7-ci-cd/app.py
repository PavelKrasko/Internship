from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from CI/CD!</h1>'

@app.route('/health')
def health():
    return 'OK', 200

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)