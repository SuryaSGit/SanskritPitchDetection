from fileinput import filename
import librosa
import matplotlib.pyplot as plt
import numpy as np
# filename = 'C:\\Users\\senth\\Downloads\\\Recordi.ogg'
filename = 'C:\\Users\\senth\\Downloads\\\Rec.ogg'
y, sr = librosa.load(filename)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr, fmin = 75, fmax = 1600)

def detect_pitch(t):
  index = magnitudes[:, t].argmax()
  pitch = pitches[index, t]

  return pitch
x=[]  

# get indexes of the maximum value in each time slice
max_indexes = np.argmax(magnitudes, axis=0)
# get the pitches of the max indexes per time slice
pitches = pitches[max_indexes, range(magnitudes.shape[1])]

#for i in range(len(pitches)):
#    x.append(detect_pitch(i))
plt.plot(pitches)
plt.show()