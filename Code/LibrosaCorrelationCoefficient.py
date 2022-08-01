from fileinput import filename
import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import euclidean
def returnpitches(filename):
  y, sr = librosa.load(filename)
  pitches, magnitudes = librosa.piptrack(y=y, sr=sr, fmin = 75, fmax = 1600)
  max_indexes = np.argmax(magnitudes, axis=0)
  # get the pitches of the max indexes per time slice
  pitches = pitches[max_indexes, range(magnitudes.shape[1])]
  y=pitches
  pitch=[]
  for i in y:
    if i!=0:
      pitch.append(i)
  return pitch
def correlation(pitcha,pitchb):
  dtw, wp=librosa.sequence.dtw(pitcha,pitchb,backtrack=True)
  i=len(wp)
  indexc=wp[:,0]
  indexd=wp[:,1]
  indexa = np.sort(indexc)
  indexb = np.sort(indexd)
  dtwpitcha=[]
  dtwpitchb=[]
  for i in indexa:
    dtwpitcha.append(pitcha[i])
  for j in indexb:
    dtwpitchb.append(pitchb[j])
  correlation=np.corrcoef(dtwpitcha,dtwpitchb)
  return correlation[0,1]
shanka = returnpitches('C:\\Users\\senth\\Downloads\\TShank1.ogg')
notshanka=returnpitches('C:\\Users\\senth\\Downloads\\TNotshank1.ogg')
oracle=returnpitches('C:\\Users\\senth\\Downloads\\shankoracle.ogg')  
shankcorrelations=[] 
notshankcorrelations=[]
shankcorrelations.append(correlation(shanka,oracle))
notshankcorrelations.append(correlation(notshanka,oracle))
print(correlation(shanka,notshanka))
print('Shankarabaranam correlation:',shankcorrelations,'Shankarabaranam correlation',notshankcorrelations)