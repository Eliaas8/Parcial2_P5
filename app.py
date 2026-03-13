from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicación Python funcionando en AWS "

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS")
        )
        return "Conexión exitosa a la base de datos"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)