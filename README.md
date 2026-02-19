# Machine Learning Music Recommender

A simple machine learning project that recommends music based on a user's age and gender using a Decision Tree classifier.

## Overview

This project:
- Trains a Decision Tree model on a small dataset
- Evaluates and tests predictions
- Exports the trained model using joblib
- Visualizes the decision tree structure

## Technologies Used

- Python
- Scikit-learn
- Pandas
- Joblib
- Jupyter Notebook

## Files

MusicRecommender.ipynb  
Primary notebook for training and testing the model.

MusicRecommender.py  
Python script version of the model.

music.csv  
Dataset used for training.

joblib/  
Contains serialized model file to avoid retraining.

Dot visualization/  
Contains exported decision tree graph (.dot file).

## How It Works

1. Load dataset
2. Train Decision Tree classifier
3. Predict music preference based on inputs
4. Save trained model using joblib
5. Load model later without retraining

## Example Prediction

Input:
Age: 21  
Gender: Male  

Output:
Recommended music genre

## Purpose

This project demonstrates:
- Basic supervised learning
- Model persistence
- Decision tree visualization
- End-to-end ML workflow

