"""Load a saved classifier and map five flex-sensor readings to a gesture."""

import os
from pathlib import Path

import joblib
import numpy as np


def load_model(model_path: str | os.PathLike[str] | None = None):
    """Load a joblib classifier from the argument or `SMART_GLOVE_MODEL`."""
    raw_path = model_path or os.environ.get("SMART_GLOVE_MODEL")
    if not raw_path:
        raise ValueError("Set SMART_GLOVE_MODEL or pass model_path.")
    path = Path(raw_path)
    if not path.exists():
        raise FileNotFoundError(f"Model file not found: {path}")
    return joblib.load(path)


def flex_to_num(data, model=None, model_path: str | os.PathLike[str] | None = None):
    """Predict one gesture from five sensor values and return its class label."""
    classifier = model if model is not None else load_model(model_path)
    features = np.asarray(data, dtype=float).reshape(1, -1)
    if features.shape[1] != 5:
        raise ValueError(f"Expected five sensor values; received {features.shape[1]}.")
    if not np.isfinite(features).all():
        raise ValueError("Sensor values must be finite numbers.")
    return classifier.predict(features)[0]
