import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# pyplot is a submodule of matplotlib

# Set colour theme
style.use("seaborn-v0_8-dark")

# List containing team strings
teams = ['Spain', 'England', 'Germany', 'Netherlands', 'Switzerland',
         'France', 'Turkey', 'Portugal', 'Austria', 'Belgium', 'Slovenia',
         'Slovakia']

# Store goals data in a dictionary
# Data from https://www.soccerstats.com/leagueview.asp?league=euro
goals_data = {
    'Goals for': [15, 8, 11, 10, 8, 4, 8, 5, 7, 2, 2, 4],
    'Goals against': [4, 6, 4, 7, 4, 3, 8, 3, 6, 2, 2, 5],
    'Goal difference': [11, 2, 7, 3, 4, 1, 0, 2, 1, 0, 0, -1],
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
# List comprehension for generating y-axis ticks
ax.set_yticks([i-2 for i in range(19)])
ax.legend(loc='upper right', ncols=3, prop="Jost", fontsize="12")

# Modify font
plt.xticks(fontfamily="Jost", fontsize="11")
plt.yticks(fontfamily="Jost", fontsize="11")

# Save figure
fig.savefig("goals_top12.png", dpi=800, transparent=False)

# Show plot
plt.show()
