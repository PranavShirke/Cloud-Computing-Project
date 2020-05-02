import matplotlib.pyplot as plt
import numpy as np

def plot_results(scores, rotate=True):
    scores_arr = np.array(scores)
    if rotate == True:
        scores_arr = scores_arr.T
    for i, step in enumerate(scores_arr):
        plt.plot(step, label='Gene'+str(i+1))
    plt.ylabel('Fitness Scores of Networks')
    plt.xlabel('Genetic Algorithm iteration')
    plt.legend()
    plt.show()

