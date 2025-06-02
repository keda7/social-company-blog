# app.py

from puppycompanyblog import app, db  # Import both app and db from your package

# Create the database tables (only run once)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
