# Model Persistence with Joblib

This folder demonstrates saving and loading a trained machine learning model
using `joblib`.

Instead of retraining the Decision Tree model every time the program runs,
the trained model is serialized and stored to disk.

## Files

- `music-recommender.joblib` – Saved trained model
- `dump.py / dump.ipynb` – Script used to save the model
- `loadExampleUsedToPredict.py` – Script used to load and use the model

## Purpose

Model persistence improves efficiency and reflects how machine learning
models are deployed in real-world systems.
