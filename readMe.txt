Simple Flashcard App

A basic web application for studying with flashcards, built with Python Flask.

Project Structure

flashcards/
    ├── app.py               # Main Flask application
    ├── flashcards.db        # SQLite database (created automatically)
    ├── static/
    │   └── style.css       # CSS styling
    └── templates/
        ├── base.html       # Base template with common layout
        ├── index.html      # Home page showing topics
        └── cards.html      # Page showing flashcards for a topic


Files Explained

app.py
- Main application file
- Contains Flask routes and database operations
- Creates database and sample data on first run
- Handles displaying topics and cards

templates/base.html
- Base template that other pages extend from
- Contains common HTML structure
- Includes CSS link and JavaScript for card flipping
- Provides navigation

templates/index.html
- Shows list of available topics
- Each topic links to its flashcards
- Extends base.html

templates/cards.html
- Displays flashcards for selected topic
- Cards can be clicked to show/hide answers
- Extends base.html

static/style.css
- Styles for the entire application
- Controls layout and appearance
- Makes cards clickable and handles show/hide

How It Works

1. Database Setup:
   - Creates SQLite database on first run
   - Adds sample flashcards if database is empty

2. Home Page (/) :
   - Shows list of unique topics from database
   - Each topic is a clickable button

3. Cards Page (/cards/<topic>):
   - Shows all flashcards for selected topic
   - Click a card to reveal its answer
   - Click again to hide answer

Setting Up

1. Run the App:

   python app.py


2. Access the App:
   - Open web browser
   - Go to: http://localhost:5000

Database Structure

Table: flashcards
- id: Unique identifier (INTEGER PRIMARY KEY)
- topic: Topic category (TEXT)
- question: Flashcard question (TEXT)
- answer: Flashcard answer (TEXT)

JavaScript Features

The app includes simple JavaScript to:
- Detect when cards are clicked
- Toggle visibility of answers
- Add/remove 'active' class for styling

Styling

CSS provides:
- Grid layout for topics
- Card-like appearance for flashcards
- Hover effects
- Responsive design
- Hidden/shown states for answers

Further Development

The app can be extended with:
1. Add/Edit/Delete cards
2. User authentication
3. Study progress tracking
4. Search functionality
5. Different card categories

Notes

- The database is created automatically when the app runs
- Sample data is only added if the database is empty
- All styling is in external CSS file
- Templates use Jinja2 for dynamic content



