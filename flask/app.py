from flask import Flask, jsonify
import psycopg2
import redis
import os

# Retrieve environment variables for database and cache
db_host = os.getenv("PGDB_HOST")
db_user = os.getenv("PGDB_USER")
db_password = os.getenv("PGDB_PASSWORD")
db_name = os.getenv("PGDB_NAME")
redis_host = os.getenv("REDIS_HOST")

# Initialize Flask app
app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host=redis_host, port=6379)

# Function to establish a connection to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    return conn

# Route to test the Flask app
@app.route('/')
def hello():
    return "Hello, Docker Multi-Container!"

# Route to get users from PostgreSQL
@app.route('/users')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

# Route to test the Redis cache
@app.route('/cache')
def cache_example():
    if cache.get('key'):
        return f"Cache Hit: {cache.get('key')}"
    else:
        cache.set('key', 'Hello from Redis Cache!')
        return "Cache Miss: Key Set"

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

