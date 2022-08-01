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
def dtw(pitcha,oracle):
  dtw, wp=librosa.sequence.dtw(pitcha,oracle,backtrack=True)
  print(wp)
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
    dtwpitchb.append(oracle[j])
  dtw=np.zeros([2,len(dtwpitcha)])
  dtw[0]=dtwpitcha
  dtw[1]=dtwpitchb
  print(len(dtwpitcha),len(dtwpitchb))
  return dtw
def correlation(pitcha,pitchb):
  correlation=np.corrcoef(pitcha,pitchb)
  return correlation[0,1]
shanka = returnpitches('C:\\Users\\senth\\Downloads\\TShank1.ogg')
notshanka=returnpitches('C:\\Users\\senth\\Downloads\\TNotshank1.ogg')
oracle=returnpitches('C:\\Users\\senth\\Downloads\\shankoracle.ogg')  
arr1=(dtw(shanka,oracle))
arr2=(dtw(notshanka,oracle))
shankdtw=arr1[0]
notshankdtw=arr2[0]
oracledtw=arr1[1]
plt.plot(shankdtw,label='shank')
plt.plot(notshankdtw,label='notshanka')
plt.plot(oracledtw,label='oracle')
plt.legend()
plt.show()
shankcorrelations=[] 
notshankcorrelations=[]
shankcorrelations.append(correlation(shankdtw,oracle))
notshankcorrelations.append(correlation(notshankdtw,oracle))
