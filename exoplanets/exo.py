
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the planetary dataset
# Source: https://exoplanetarchive.ipac.caltech.edu/
planets = pd.read_csv("planets.csv", sep=',', comment='#')

sns.set_theme(style="ticks")

# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")

# Plot the orbital period with horizontal boxes
sns.boxplot(x="st_mass", y="sy_pnum", data=planets)

# Add in points to show each observation
sns.stripplot(x="st_mass", y="sy_pnum", data=planets,
              size=2, color=".3", linewidth=0)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)
