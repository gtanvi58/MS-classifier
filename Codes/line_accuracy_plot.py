'''
Compare the accuracies of various model configurations for two loss functions
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Generated Model Name": ["Model 0", "Model 1", "Model 1", "Model 2", "Model 2",
                             "Model 3", "Model 3","Model 4", "Model 5", "Model 6"],
    "Test Set": ["manifesto", "supramacist", "manifesto", "suicide", "manifesto",
                 "terrorist", "manifesto", "manifesto", "manifesto", "manifesto"],
    "Test Accuracy Cross Entropy": [89.79, 97, 48.61, 92, 59.28, 88, 64.16, 60.26, 97.06, 97.03],
    "Test Accuracy N-Pair": [94.46, 86.25, 61.56, 90.66, 60.91, 85.6, 58.63, 62.21, 98.04, 97.87]
}
df = pd.DataFrame(data)

# Filter for 'manifesto' test set
df_manifesto = df[df['Test Set'] == 'manifesto']
plt.figure(figsize=(12, 6))

# Plot for Test Accuracy Cross Entropy
sns.lineplot(x="Generated Model Name", y="Test Accuracy Cross Entropy", marker="o", data=df_manifesto, label='Cross Val', palette="viridis")

# Plot for Test Accuracy N-Pair
sns.lineplot(x="Generated Model Name", y="Test Accuracy N-Pair", marker="o", data=df_manifesto, label='N-Pair', palette="viridis")

plt.title('Mistral: Trend of Test Accuracy on Manifesto Dataset Across Different Model Configurations')
plt.xlabel('Model Configuration')
plt.ylabel('Accuracy')
plt.legend(title='Loss Function')
plt.show()