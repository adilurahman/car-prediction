# Car Price Prediction (Flask)

A small Flask web application for predicting car prices using a trained regression model.

## Overview

This project provides a simple web UI and backend for serving a regression model that predicts car prices from input features. It includes training utilities, a classifier module (model wrapper), and a Flask app to serve predictions.

## Features

- Train and save a regression model (`train_reg.py`).
- Serve predictions via a Flask web app (`app.py`, `wsgi.py`).
- Simple web UI in `templates/index.html` for interactive predictions.
## Demo Video

https://github.com/user-attachments/assets/8841f5a2-4466-4848-9067-60e461ba6f6b


## Requirements

- Python 3.8+ (recommended)
- See `requirements.txt` for exact dependencies.

## Installation

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Usage

- To run the Flask app locally:

```powershell
python app.py
```

- Open your browser at http://127.0.0.1:5000 to use the web UI.

## Training

- Use `train_reg.py` to train a model and save the artifact used by the app. Check the top of that file for training parameters and dataset locations.

## Important Files

- `app.py` — Flask application that serves the UI and prediction endpoint.
- `classifier.py` — Model loading and prediction helpers.
- `train_reg.py` — Training script for the regression model.
- `wsgi.py` — WSGI entrypoint for deployment.
- `templates/index.html` — Frontend HTML for submitting prediction requests.

## Notes

- Confirm model artifact paths in `classifier.py` before running the app.
- This repository is intended as a lightweight demo; adjust data validation and security for production use.

## License & Contribution

Feel free to open issues or submit pull requests to improve functionality or documentation.

## Hosted Link
https://dashboard.render.com/web/srv-d604kj2li9vc73ancgkg
