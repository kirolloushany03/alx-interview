#!/usr/bin/python3
"""
This module solves the island perimeter problem.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Loops through the grid and checks each land cell (1). If the
    neighboring cell is water (0) or out of bounds, it adds to the perimeter.
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:

                if i == 0 or grid[i - 1][j] == 0:
                    count += 1

                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    count += 1

                if j == 0 or grid[i][j - 1] == 0:
                    count += 1

                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    count += 1
    return count
