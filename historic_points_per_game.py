import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# Dictionary to store points per game for each team
team_ppg = {"Spain": [1.50, 1.67, 3.00],
            "England": [1.25, 2.43, 1.71],
            "Germany": [1.83, 1.00, 2.00],
            "Netherlands": [2.25, 1.67],
            "Switzerland": [1.50, 1.20, 1.80],
            "France": [2.29, 1.50, 1.50],
            "Turkey": [0.00, 1.80],
            "Portugal": [1.86, 1.00, 1.60],
            "Austria": [0.33, 1.50, 1.50],
            "Belgium": [1.80, 2.40, 1.00]}

xticks = ['Euro 2016', 'Euro 2021', 'Euro 2024']

# Set the font family, style and size using the 'font_manager' library
legendfont = font_manager.FontProperties(family='Jost',
                                   weight='normal',
                                   style='normal', size=11)

# List comprehension to create x values
x_axis = [x for x in range(len(xticks))]

fig, ax = plt.subplots()

markers = ['o', 'x', 'p', '^', 's']

m = 0   # Counter

# Extract key-value pairs from dictionary using the items method
for key, value in team_ppg.items():

    if len(value) < len(xticks):
        # Two teams did not take part in 2016, so have a condition
        # to handle this
        ax.plot(x_axis[1:], value, label=key, marker=markers[m])
    else:
        ax.plot(x_axis, value, label=key, marker=markers[m])

    if m >= len(markers)-1:
        m = 0
    else:
        m += 1

    print(key)
    print(value)

# 2016 winner label - Portugal
portugal2016_ppg = team_ppg["Portugal"][0]
plt.text(-0.05, portugal2016_ppg + 0.1, str(portugal2016_ppg) + " POR", fontname="Jost")

# 2021 winner label - Italy - added as a point
ax.plot(1, 2.43, marker="x", color="red")
plt.text(1, 2.5, str(2.5) + " ITA", fontname="Jost")

# 2021 winner label - Italy
spain2024_ppg = team_ppg["Spain"][2]
plt.text(1.9, spain2024_ppg-0.2, str(spain2024_ppg) + " ESP", fontname="Jost")

plt.xticks(x_axis, xticks, fontfamily="Jost", fontsize=11)
plt.yticks(fontfamily="Jost", fontsize=11)

# fig.tight_layout()
# fig.legend()

# Moving the legend box
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5), prop=legendfont)
plt.title("Average points per game for the top 10 teams of Euro 2024", fontsize=13, fontname="Jost")
plt.ylabel("Points")

# Save figure as a png
plt.savefig("teams_ppg.png", dpi=600, transparent=False)

# Display plot
plt.show()
