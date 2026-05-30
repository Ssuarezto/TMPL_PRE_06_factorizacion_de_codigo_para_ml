import os
import pickle


def save_model(model, save_path="models/estimator.pkl"):
    """Save the model to the specified path."""
    directory = os.path.dirname(save_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    with open(save_path, "wb") as file:
        pickle.dump(model, file)
