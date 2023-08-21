import matplotlib.pyplot as plt

plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "white",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})

x = range(1,25)
y = range(60,108)[::-2]
y2 = range(16,40)[::-1]

plt.bar(x, y,  label='One')
plt.bar(x, y2, label='Two')
plt.grid()
plt.xticks(x)

plt.xlabel('Hour of day')
plt.ylabel('Value')
plt.title('E', color="w")
plt.legend()
plt.tight_layout()
plt.style.use("dark_background")
plt.show()