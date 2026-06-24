from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Docker Compose!</h1>'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/db')
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'db'),
            database=os.getenv('DB_NAME', 'postgres'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', 'mysecret')
        )
        conn.close()
        return '<h1>DB connection: OK</h1>'
    except Exception as e:
        return f'<h1>DB Error: {e}</h1>', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)