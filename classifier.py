import pickle
import importlib.util
import sys


class DummyModel:
    """A tiny fallback model used when the real model cannot be loaded.

    It implements a `predict` method that returns a simple constant value
    or a basic heuristic so the Flask app can run without scikit-learn/scipy.
    """

    def predict(self, X):
        # Return a constant prediction for each row (5.0 lakhs)
        try:
            n = len(X)
        except Exception:
            n = 1
        return [5.0] * n


def load_model():
    """Attempt to load `model.pkl`. If scikit-learn (and its wheels) aren't
    available, or loading fails, return a `DummyModel` instead.
    """
    # If scikit-learn is not installed, avoid attempting to unpickle which
    # would import sklearn and may hang on systems without binary wheels.
    if importlib.util.find_spec("sklearn") is None:
        print("⚠️ sklearn not found — using DummyModel fallback.")
        return DummyModel()

    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        # Don't crash the whole app for unpickling/import issues — fall back.
        print(f"⚠️ Failed to load model.pkl: {e}; using DummyModel fallback.")
        return DummyModel()

