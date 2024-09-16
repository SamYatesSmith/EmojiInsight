# Helper functions

import matplotlib.pyplot as plt

def plot_correlation_matrix(df):
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True)
    plt.show()
