import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    """Connexion a postgreSQL"""
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'db'),
            database=os.environ.get('DB_NAME', 'forum_db'),
            user=os.environ.get('DB_USER', 'forum_user'),
            password=os.environ.get('DB_PASSWORD', 'forum_password')
        )
        return conn
    except Exception as e:
        print("Erreur de connexion a la base de donnees:", e)
        return None

def init_db():
    """Initialisation de la table"""
    retries = 5
    while retries > 0:
        conn = get_db_connection()
        if conn:
            with conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS messages (
                        id SERIAL PRIMARY KEY,
                        pseudo VARCHAR(100) NOT NULL,
                        content TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                ''')
            conn.commit()
            conn.close()
            print("Table creee", flush=True)
            return
        print("Retrying", flush=True)
        time.sleep(2)
        retries -= 1

@app.route('/messages', methods=['GET'])
def get_messages():
    """Recuperation des messages"""
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erreur de connexion DB"}), 500
    
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM messages ORDER BY created_at DESC;")
        messages = cur.fetchall()
    conn.close()
    
    return jsonify(messages), 200

@app.route('/messages', methods=['POST'])
def add_message():
    """Ajout nouveau message"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Aucune donnee"}), 400

    pseudo = data.get('pseudo')
    content = data.get('content')
    
    if not pseudo or not content:
        return jsonify({"error": "pseudo et content requis"}), 400
        
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erreur de connexion DB"}), 500
        
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO messages (pseudo, content) VALUES (%s, %s)",
            (pseudo, content)
        )
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Message publie"}), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
