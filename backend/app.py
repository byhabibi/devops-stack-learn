from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db():
    conn = psycopg2.connect(
        host="postgres",
        database="appdb",
        user="dba",
        password="dba123"
    )
    return conn

@app.route("/")
def home():
    return {"message": "Backend API running bro 🔥"}

@app.route("/db")
def db_test():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        conn.close()
        return {"db": str(version)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
