import cv2
import numpy as np


def compare_images(expected_path, actual_path):

    expected = cv2.imread(expected_path)
    actual = cv2.imread(actual_path)

    if expected is None:
        raise FileNotFoundError(
            f"Expected image not found: {expected_path}"
        )

    if actual is None:
        raise FileNotFoundError(
            f"Actual image not found: {actual_path}"
        )

    if expected.shape != actual.shape:
        return 0.0

    difference = cv2.absdiff(expected, actual)

    mean_difference = np.mean(difference)

    similarity = 100 - mean_difference

    return similarity