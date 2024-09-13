import heatmap_functions as hmap
import numpy as np
import matplotlib.pyplot as plt

# Create a numpy array of lists to store heatmap data
grid = np.array([[46, 58, 59, 76, 48, 59, 66],
                [54, 49, 74, 63, 52, 59, 34],
                [73, 70, 67, 55, 52, 0, 0],
                [66, 37, 53, 65, 60, 41, 0],
                [51, 53, 33, 49, 52, 0, 0],
                [48, 63, 58, 56, 40, 41, 0],
                [56, 43, 69, 39, 40, 0, 0],
                [74, 57, 73, 73, 60, 0, 0],
                [52, 53, 47, 61, 0, 0, 0],
                [61, 55, 60, 56, 0, 0, 0],
                [32, 39, 26, 27, 0, 0, 0],
                [39, 56, 59, 37, 0, 0, 0]])

# Create figure and axes
fig, ax = plt.subplots()

# National teams stored as list items
row_labels = ['Spain', 'England', 'Germany', 'Netherlands', 'Switzerland',
              'France', 'Turkey', 'Portugal', 'Austria', 'Belgium', 'Slovenia',
              'Slovakia']

# Create list with for-loop
column_labels = [1 + i for i in range(7)]

# Labels for columns (game number)
col_labels = ['1', '2', '3', '4', '5', '6', '7']

# cmap argument sets colour scheme
# heatmap function returns both an image of the grid and the colour bar on the side
# 'heatmap' is defined in the matplotlib documentation and is slightly modified in this
# case to change fonts
image, cbar = hmap.heatmap(grid, row_labels, column_labels, cmap="Blues")

# Iterate over the rows and columns to add in the cell values as text
for i in range(len(row_labels)):
    for j in range(len(column_labels)):
        # Do not label cells with a zero value :)
        text_value = grid[i, j]
        if text_value > 0:
            text = ax.text(j, i, grid[i, j], ha="center", va="center", color="w", fontfamily="Lato")

# Set layout style
fig.tight_layout()

# Show graph
plt.show()
