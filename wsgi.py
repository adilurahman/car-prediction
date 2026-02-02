"""WSGI entry point for gunicorn deployment."""
from app import app

if __name__ == "__main__":
    app.run()
