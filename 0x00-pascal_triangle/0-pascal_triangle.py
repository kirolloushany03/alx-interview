#!/usr/bin/python3
"""
Generates Pascal's triangle up to the nth row.

    Pascal's triangle is a triangular array of binomial coefficients.
    Each number is the sum of the two directly above it.

    Args:
        n (int): The number of rows in Pascal's triangle to generate.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
        Each inner list contains the integers of that row in the triangle.
        Returns an empty list if n <= 0.
"""


def pascal_triangle(n):
    """
    solving pascals triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
