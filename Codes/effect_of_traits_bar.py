'''
Analyze the effect of identified traits on the accuracy of the model when tested on the mass shooter manifesto dataset
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pastel_palette = sns.color_palette("deep")

# Data from the table
models = ['Mistral+Supramacist', 'Mistral+Suicidal', 'Mistral+Terrorist', 'Mistral+Manifesto']
n_pair_accuracy = [97.35, 94.66, 98.33, 89.79]

# Setting the positions and width for the bars
x = np.arange(len(models))
width = 0.35

# Creating the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the bars
bars2 = ax.bar(x, n_pair_accuracy, width, label='Test Accuracy N-Pair', color=pastel_palette[0])

# Adding labels and title
ax.set_xlabel('Fine Tuning Trait')
ax.set_ylabel('Accuracy (%)')
ax.set_title('Effect of various fine tuning traits on the accuracy when tested on Mass Shooter dataset')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

# Adding the values on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars2)

# Displaying the plot
plt.show()
