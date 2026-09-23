import os
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )

@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    if not name or not description:
        return jsonify({"error": "Missing name or description"}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
    conn.commit()
    conn.close()
    return jsonify({"status": "Item created"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
