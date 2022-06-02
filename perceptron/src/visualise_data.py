"""
Visualise data
"""

import seaborn
import matplotlib.pyplot as plt


def plot_dataset(dataset, dataset_title, save_path):
    """Creates plot of given dataset

    :param dataset: Dataset to plot
    :type dataset: dict
    :param dataset_title: Title for dataset plot
    :type dataset_title: str
    :param save_path: Path to save plot image
    :type save_path: str
    """

    BORDER_CONST = 25

    x_plus = []
    y_plus = []
    x_minus = []
    y_minus = []

    for point in dataset:
        if dataset[point] == 1:
            x_plus.append(point[0])
            y_plus.append(point[1])
        elif dataset[point] == -1:
            x_minus.append(point[0])
            y_minus.append(point[1])

    # find minimum values across axes
    x_min = min(x_plus + x_minus) - BORDER_CONST
    x_max = max(x_plus + x_minus) + BORDER_CONST
    y_min = min(y_plus + y_minus) - BORDER_CONST
    y_max = max(y_plus + y_minus) + BORDER_CONST

    fig = plt.figure()
    ax = plt.axes(
        xlim=(x_min, x_max),
        ylim=(y_min, y_max)
    )
    plt.scatter(x_plus, y_plus, marker="+", c="green", s=128, linewidths=2)
    plt.scatter(x_minus, y_minus, marker="_", c="red", s=128, linewidths=2)

    plt.title(dataset_title)
    plt.savefig(save_path)
