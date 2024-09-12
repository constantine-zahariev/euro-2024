import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# pyplot is a submodule of matplotlib

# Set colour theme
style.use("seaborn-v0_8-dark")

# List containing team strings
teams = ['Romania', 'Italy', 'Ukraine', 'Georgia', 'Denmark',
         'Hungary', 'Serbia', 'Croatia', 'Albania', 'Czechia', 'Poland',
         'Scotland']

# Store goals data in a dictionary
goals_data = {
    'Goals for': [4, 3, 2, 5, 2, 2, 1, 3, 3, 3, 3, 2],
    'Goals against': [6, 5, 4, 8, 4, 5, 2, 6, 5, 5, 6, 7],
    'Goal difference': [-2, -2, -2, -3, -2, -3, -1, -3, -2, -2, -3, -5],
}

x = np.arange(len(teams))   # Create index list for teams list using numpy
bar_width = 0.25
multiplier = 0

# Create figure and axes, set layout style
fig, ax = plt.subplots(layout="tight")

# for-loop extracts dictionary contents
# ax.bar uses extracted key, value pairs
for metric, value in goals_data.items():
    # Purpose of 'offset' is to shift along bars plotted
    offset = bar_width*multiplier
    rects = ax.bar(x + offset, value, bar_width, label=metric)
    ax.bar_label(rects, padding=3, fontfamily="Jost")
    multiplier += 1

# Set title, axes labels and legend
ax.set_title("Goals for, against and goal difference", fontfamily='Jost', fontsize="15")
ax.set_ylabel("Goals", fontfamily="Jost", fontsize="12")
ax.set_xticks(x + bar_width, teams, rotation=60)
ax.set_yticks([i-5 for i in range(16)])
ax.legend(loc='upper right', ncols=3, prop="Jost", fontsize="12")

# Modify font
plt.xticks(fontfamily="Jost", fontsize="11")
plt.yticks(fontfamily="Jost", fontsize="11")

# Save figure
plt.savefig("goals_last12.png", dpi=800, transparent=False)

# Show plot
plt.show()

