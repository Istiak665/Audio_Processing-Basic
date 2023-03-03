# -*- coding: utf-8 -*-
"""checking_single_mixed-audios.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Irt6HLN_mEt8BbjF8lVI62VM2Pquse_A
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from IPython.display import Audio

bulldozer = "/content/drive/MyDrive/Construction Equipment Activity/Feature Extraction/audio/bulldozer_wav"
dump_truck = "/content/drive/MyDrive/Construction Equipment Activity/Feature Extraction/audio/dump_truck_wav"
mixed = "/content/drive/MyDrive/Construction Equipment Activity/Feature Extraction/audio/mixed"
SAMPLE_RATE = 44100

def read_load_audios(path, sample_rate):
  signal = []

  files = os.listdir(path)

  for item in files:
    if item.endswith('.wav'):
      wave_files = os.path.join(path, item)
      data, sr = librosa.load(wave_files, sr=sample_rate)
      signal.append(data)

  return np.array(signal), sr

"""## Bulldozer"""

bull_values, bull_sr = read_load_audios(bulldozer, sample_rate=SAMPLE_RATE)
print(bull_values.shape)

"""## Dump Truck"""

dump_values, dump_sr = read_load_audios(dump_truck, sample_rate=SAMPLE_RATE)
print(dump_values.shape)

"""## Mixed"""

mixed_values, mixed_sr = read_load_audios(mixed, sample_rate=SAMPLE_RATE)
print(mixed_values.shape)

"""## Play each and mixed signal"""

# Play any sound of bulldozer
Audio(bull_values[2], rate=SAMPLE_RATE)

# Play any sound of dump truck
Audio(dump_values[2], rate=SAMPLE_RATE)

# Play any sound of mixed sound
Audio(mixed_values[2], rate=SAMPLE_RATE)

"""## Plot each and mixed raw signal"""

# Let's plot bulldozer
plt.plot(bull_values[2])

# Let's plot dump truck
plt.plot(dump_values[2])

# Let's plot mixed sound
plt.plot(mixed_values[2])

# Let's plot bulldozer
plt.plot(bull_values[2][20000:21000])

# Let's plot dump truck
plt.plot(dump_values[2][20000:21000])

# Let's plot mixed sound
plt.plot(mixed_values[2][20000:21000])