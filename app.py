from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine, text
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('flashcards.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            difficulty TEXT NOT NULL
        )
    ''')
    
    # Check if table is empty
    cursor = conn.execute('SELECT COUNT(*) FROM flashcards')
    if cursor.fetchone()[0] == 0:
        # Only insert sample data if table is empty
        sample_cards = [
            ('Software Development', 'What is a variable?', 'A container that holds data','Easy'),
            ('Software Development', 'What is a function?', 'A reusable block of code','Easy'),
            ('Networks', 'What is IP?', 'Internet Protocol - rules for sending data','Medium'),
            ('Networks', 'What is HTTP?', 'Protocol for transferring web pages','Medium'),
            ('Databases', 'What is SQL?', 'Language used to query databases','Easy')
        ]
        
        conn.executemany('INSERT INTO flashcards (topic, question, answer,difficulty) VALUES (?, ?, ?, ?)', 
                         sample_cards)
        conn.commit()
    
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    topics = conn.execute('SELECT DISTINCT topic FROM flashcards').fetchall()
    diff_levels = conn.execute('SELECT DISTINCT difficulty FROM flashcards').fetchall()
    conn.close()
    return render_template('index.html', topics=topics, diff_levels=diff_levels )

@app.route('/cards/<topic>')
def cards(topic):
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards WHERE topic = ?', 
                            (topic,)).fetchall()
    conn.close()
    return render_template('cards.html', cards=flashcards, topic=topic)


@app.route('/cards_diff/<difficulty>')
def cards_diff(difficulty):
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards WHERE difficulty = ?', 
                            (difficulty,)).fetchall()
    conn.close()
    return render_template('cards_diff.html', cards=flashcards, difficulty=difficulty)


@app.route('/maintain')
def maintain():
    conn = get_db_connection()
    flashcards = conn.execute('SELECT * FROM flashcards').fetchall()
    conn.close()
    return render_template('maintain.html', cards=flashcards)


@app.route('/add_card', methods=['POST', 'GET'])
def add_card():
    if request.method == 'POST':
        topic = request.form['topic']
        question = request.form['question']
        answer = request.form['answer']
        difficulty = request.form['difficulty']
        conn = get_db_connection()
        conn.execute('INSERT INTO flashcards (topic, question, answer, difficulty) VALUES (?, ?, ?, ?)',
                    (topic, question, answer, difficulty))
        conn.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_card.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_card(id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        topic = request.form.get('topic')
        question = request.form.get('question')
        answer = request.form.get('answer')
        difficulty = request.form['difficulty']
        conn.execute('UPDATE flashcards SET topic = ?, question = ?, answer = ?, difficulty = ? WHERE id = ?',
                    (topic, question, answer, difficulty, id))
        conn.commit()
        conn.close()
        return redirect(url_for('maintain'))
    
    card = conn.execute('SELECT * FROM flashcards WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('update_card.html', card=card)

@app.route('/delete/<int:id>')
def delete_card(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM flashcards WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('maintain'))
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
