'''
Plot a grouped bar graph to compare accuracies of various fine tuning approaches used for two loss functions
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pastel_palette = sns.color_palette("deep")

# Data from the table
models = ['Baseline: Mistral', 'Multistage: Mistral', 'Ensemble: Mistral', 'Baseline: BERT', 'Multistage: BERT']
cross_val_accuracy = [89.79, 60.26, 77.82, 97.06, 98.04]
n_pair_accuracy = [94.46, 62.21, 80.13, 97.03, 97.87]

# Setting the positions and width for the bars
x = np.arange(len(models))
width = 0.35

# Creating the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the bars
bars1 = ax.bar(x - width/2, cross_val_accuracy, width, label='Test Accuracy Cross Entropy', color=pastel_palette[0])
bars2 = ax.bar(x + width/2, n_pair_accuracy, width, label='Test Accuracy N-Pair', color=pastel_palette[1])

# Adding labels and title
ax.set_xlabel('Training Approach')
ax.set_ylabel('Accuracy (%)')
ax.set_title('Accuracy Comparison for different Fine Tuning Approaches')
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

add_labels(bars1)
add_labels(bars2)

# Displaying the plot
plt.show()
