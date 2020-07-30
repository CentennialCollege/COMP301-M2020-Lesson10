"""Dynamically graphing frequencies of die rolls """
from matplotlib import animation
import matplotlib.pyplot as plt
import random
from matplotlib.pyplot import xlabel, ylabel
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame"""

    random.seed(45)
    #roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1

    #reconfigure plot for updated die frequencies
    plt.cla() # clear old contents of current figure
    axes = sns.barplot(faces, frequencies, palette="bright") # new bars
    axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) *1.10) # scale y-axis by 10%

    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_with() * 0.5
        text_y = bar.get_height()
        text=f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')