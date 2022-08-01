import parselmouth
from IPython.display import Audio
filename = parselmouth.Sound("C:\\Users\\senth\\Downloads\\testtone.wav")
Audio(data=(filename.values), rate=(filename.sampling_frequency))
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def plotOnGraph(pitch, color):
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2.5, color=color)
    
def setupGraph(ymin, ymax):
    sns.set() # Use seaborn's default style to make attractive graphs
    plt.rcParams['figure.dpi'] = 150 # Show images nicely
    plt.figure()
    plt.ylim(ymin, ymax)
    plt.ylabel("frequency [Hz]")
    plt.xlabel("seconds")
    plt.grid(True)
pitchZh = filename.to_pitch()

setupGraph(50, 375)

plotOnGraph(pitchZh, 'r')


plt.gca().legend(('zh','en','he'))

plt.show()