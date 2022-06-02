"""
Handles dataset creation
"""

import random


def generate_training_set(num_points):
    """ Creates training dataset for function y = 45 - x

    :param num_points: number of dataset samples
    :type num_points: int
    :return: training dataset
    :rtype: dict
    """
    x_coordinates = [random.randint(0, 50) for i in range(num_points)]
    y_coordinates = [random.randint(0, 50) for i in range(num_points)]
    training_set = dict()

    for x, y in zip(x_coordinates, y_coordinates):
        if y <= 45 - x:
            training_set[(x, y)] = 1
        elif y > 45 - x:
            training_set[(x, y)] = -1
    return training_set



