import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from IPython.display import Audio

bulldozer = "audio/bulldozer_wav"
dump_truck = "audio/dump_truck_wav"
SAMPLE_RATE = 44100

# For single Folder Folder
def mel_spectrogram(path, sample_rate):
    signals = []
    melspec_list = []
    
    files = os.listdir(path)
    for item in files:
        if item.endswith('.wav'):
            files = os.path.join(path, item)
            y, sr = librosa.load(files, sr=sample_rate)
            signals.append(y)
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
            melspec = librosa.power_to_db(S).astype(np.float32)
            melspec_list.append(melspec)
#             mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=30)
#             mfcc_list.append(mfcc)
            
    return np.array(melspec_list), sr
    
    
# Bulldozer wav values
bulldozer_melspec, sr = mel_spectrogram(bulldozer, SAMPLE_RATE)
print(bulldozer_melspec.shape)


librosa.feature.mfcc(S=librosa.power_to_db(bulldozer_melspec[0]))

array([[-742.3991   , -742.3991   , -742.3991   , ..., -571.5384   ,
        -633.1076   , -609.43195  ],
       [   0.       ,    0.       ,    0.       , ...,  201.47263  ,
         145.65869  ,  173.37009  ],
       [   0.       ,    0.       ,    0.       , ...,  111.70987  ,
         121.49762  ,  135.19893  ],
       ...,
       [   0.       ,    0.       ,    0.       , ...,   65.85601  ,
          45.16886  ,   14.447916 ],
       [   0.       ,    0.       ,    0.       , ...,   59.47354  ,
          26.499176 ,    3.6974907],
       [   0.       ,    0.       ,    0.       , ...,   12.402262 ,
           6.568433 ,  -11.282288 ]], dtype=float32)
           
import librosa.display

plt.figure(figsize=(10, 5))
librosa.display.specshow(bulldozer_melspec[9], x_axis='time')
plt.colorbar()
plt.tight_layout()
plt.title('BULLDOZER AND DUMP_TRUCK 10')
plt.show


import librosa.display
librosa.display.specshow(bulldozer_melspec[0], x_axis='time',  y_axis='mel', sr=sr, fmax=16000)


audios = os.listdir(bulldozer)
print(audios)

output_dir = "audio/mixed"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
    
for audio in audios:
    for melspec in bulldozer_melspec:
        
        dpi = 300
        width = 12
        height = 8
        fig = plt.figure(figsize=(width, height), dpi=dpi, frameon=False)
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(True)
        
        outputFile = output_dir + "/" + os.path.splitext(audio)[0]
        librosa.display.specshow(melspec, y_axis='linear')
        plt.savefig(outputFile+str()+'.jpg', figsize=(width, height), bbox_inches='tight',
                    pad_inches=0, dpi=dpi, orientation ='landscape', transparent = True,)
