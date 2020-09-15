"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: A 2D data array containing inflammation data (each row contains measurments for a single day).
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: A 2D data array containing inflammation data (each row contains measurments for a single day).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: A 2D data array containing inflammation data (each row contains measurments for a single day).
    :returns: An array of min values of measurements for each day.
    """
    return np.min(data, axis=0)


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
