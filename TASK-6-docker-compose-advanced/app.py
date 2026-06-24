from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Production Compose!</h1>'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/db')
def db_check():
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        conn.close()
        return '<h1>DB connection: OK</h1>'
    except Exception as e:
        return f'<h1>DB Error: {e}</h1>', 500

@app.route('/redis')
def redis_check():
    try:
        r = redis.from_url(os.getenv('REDIS_URL'))
        r.ping()
        return '<h1>Redis connection: OK</h1>'
    except Exception as e:
        return f'<h1>Redis Error: {e}</h1>', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)