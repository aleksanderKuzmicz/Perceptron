"""
Main module
"""
from src.configuration.const import *
from src.create_dataset import generate_training_set
from src.visualise_data import plot_dataset

DATASET_SIZE = 30

train_dataset = generate_training_set(DATASET_SIZE)
plot_dataset(train_dataset, "Training dataset", PATH_TRAIN_DATASET_PLOT)
