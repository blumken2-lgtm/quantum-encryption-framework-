# aperiodic_tiling.py

"""
Module handling the mathematics and implementation of aperiodic tiling.
Provides utilities for generating and validating non-repeating tile patterns.
"""

import matplotlib.pyplot as plt
import numpy as np

def generate_hat_pattern(rows=10, columns=10):
    """
    Generates a non-repeating 'hat' tile pattern.

    Args:
        rows (int): Number of rows in the pattern.
        columns (int): Number of columns in the pattern.

    Returns:
        np.ndarray: A 2D array representing the non-repeating pattern.
    """
    # Placeholder: Use a simple pseudo-aperiodic generation method for now.
    pattern = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            pattern[i, j] = (i * j) % (rows // 2 + 1)
    return pattern

def validate_hat_pattern(pattern):
    """
    Validates that the provided pattern is non-repeating.

    Args:
        pattern (np.ndarray): The pattern to validate.

    Returns:
        bool: True if the pattern is valid, False otherwise.
    """
    # A simple check: ensure no row or column is identical.
    rows_unique = len(np.unique(pattern, axis=0)) == pattern.shape[0]
    cols_unique = len(np.unique(pattern, axis=1)) == pattern.shape[1]
    return rows_unique and cols_unique

def visualize_hat_pattern(pattern):
    """
    Visualizes the aperiodic tiling pattern.

    Args:
        pattern (np.ndarray): The pattern to visualize.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(pattern, cmap='tab10', interpolation='nearest')
    plt.colorbar()
    plt.title("Aperiodic Hat Pattern")
    plt.show()

# Example usage: Uncomment the following lines to test the module
# if __name__ == "__main__":
#     pattern = generate_hat_pattern(10, 10)
#     print("Pattern:")
#     print(pattern)
#     print("Valid Pattern:", validate_hat_pattern(pattern))
#     visualize_hat_pattern(pattern)