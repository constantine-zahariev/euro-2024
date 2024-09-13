import heatmap_functions as hmap
import numpy as np
import matplotlib.pyplot as plt

# Create a numpy array of lists to store heatmap data
grid = np.array([[28, 45, 41, 35, 0, 0, 0],
                [69, 42, 54, 51, 0, 0, 0],
                [72, 44, 40, 0, 0, 0, 0],
                [44, 38, 27, 24, 0, 0, 0],
                [68, 51, 54, 45, 0, 0, 0],
                [49, 30, 42, 0, 0, 0, 0],
                [46, 61, 46, 0, 0, 0, 0],
                [54, 67, 46, 0, 0, 0, 0],
                [31, 33, 41, 0, 0, 0, 0],
                [26, 62, 31, 0, 0, 0, 0],
                [34, 47, 42, 0, 0, 0, 0],
                [27, 47, 58, 0, 0, 0, 0]])

# Create figure and axes
fig, ax = plt.subplots()

# National teams stored as list items
row_labels = ['Romania', 'Italy', 'Ukraine', 'Georgia', 'Denmark',
              'Hungary', 'Serbia', 'Croatia', 'Albania', 'Czechia', 'Poland',
              'Scotland']

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
        # Do not label cell unless there's a nonzero value :)
        text_value = grid[i, j]
        if text_value > 0:
            text = ax.text(j, i, grid[i, j], ha="center", va="center",
                           color="w", fontfamily="Jost", fontsize=11)

# Set layout style
fig.tight_layout()

# Save figure as a png
plt.savefig("possession_last12.png", dpi=600, transparent=False)

# Show graph
plt.show()
