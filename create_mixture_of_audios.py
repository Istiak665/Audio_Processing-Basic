import librosa
import os
import glob
import soundfile as sf
import numpy as np

## //.............Mixing of Two audios from Two Different Folders..............//

directory1 = 'path/to/directory1'
directory2 = 'path/to/directory2'
output_dir = 'path/to/output/directory'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Find the maximum length of the audio files
max_length = 0
for audio_path in glob.glob(os.path.join(directory1, "*.wav")):
    y, sr = librosa.load(audio_path, sr=None)
    max_length = max(max_length, len(y))
for audio_path in glob.glob(os.path.join(directory2, "*.wav")):
    y, sr = librosa.load(audio_path, sr=None)
    max_length = max(max_length, len(y))

# Loop through all audio files in the input directories and mix them together
mix_num = 1
for audio_path1, audio_path2 in zip(glob.glob(os.path.join(directory1, "*.wav")),
                                    glob.glob(os.path.join(directory2, "*.wav"))):
    y1, sr1 = librosa.load(audio_path1, sr=None)
    y2, sr2 = librosa.load(audio_path2, sr=None)
    y1 = librosa.util.fix_length(y1, size=max_length)
    y2 = librosa.util.fix_length(y2, size=max_length)
    y_mix = y1 + y2

    output_path = os.path.join(output_dir, f"mix{mix_num}.wav")
    if os.path.isfile(output_path):
        os.remove(output_path)

    sf.write(output_path, y_mix, sr1)
    mix_num += 1

print("Done!")


## //.............Mixing of Three audios from Three Different Folders..............//

directory1 = 'path/to/directory1'
directory2 = 'path/to/directory2'
directory3 = 'path/to/directory3'

# Set the directory paths for input and output
input_dirs = [directory1, directory2, directory3]
output_dir = 'path/to/output/directory'

# Find the maximum length of the audio files
max_length = 0
for input_dir in input_dirs:
    for audio_path in glob.glob(os.path.join(input_dir, "*.wav")):
        y, sr = librosa.load(audio_path, sr=None)
        max_length = max(max_length, len(y))

# Loop through all audio files in the input directories and concatenate them
y_concat = None
sr_concat = None
for input_dir in input_dirs:
    for i, audio_path in enumerate(glob.glob(os.path.join(input_dir, "*.wav"))):
        y, sr = librosa.load(audio_path, sr=None)
        y = librosa.util.fix_length(y, size=max_length)
        if y_concat is None:
            y_concat = y
            sr_concat = sr
        else:
            # Mix the audio files
            y_concat = 0.5 * (y_concat + y)

    # Save the mixed audio to file
    output_path = os.path.join(output_dir, "mix{}.wav".format(input_dir))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if os.path.isfile(output_path):
        os.remove(output_path)

    if y_concat is not None and len(y_concat) > 0:
        sf.write(output_path, y_concat, sr_concat)
    else:
        print("Error: No audio data to write to file.")

## //.............Mixing of Three audios from Three Different Folders..............//

directory1 = 'input_directory_1'
directory2 = 'input_directory_2'
directory3 = 'input_directory_3'
directory4 = 'input_directory_4'

# Set the directory paths for input and output
input_dirs = [directory1, directory2, directory3, directory4]
output_dir = 'output_directory'

# Find the maximum length of the audio files
max_length = 0
for input_dir in input_dirs:
    for audio_path in glob.glob(os.path.join(input_dir, '*.wav')):
        y, sr = librosa.load(audio_path, sr=None)
        max_length = max(max_length, len(y))

# Loop through all audio files in the input directories and concatenate them
y_concat = None
sr_concat = None
for audio_idx in range(min([len(glob.glob(os.path.join(input_dir, '*.wav'))) for input_dir in input_dirs])):
    y_mix = None
    for input_dir in input_dirs:
        audio_path = glob.glob(os.path.join(input_dir, '*.wav'))[audio_idx]
        y, sr = librosa.load(audio_path, sr=None)
        y = librosa.util.fix_length(y, size=max_length)
        if y_mix is None:
            y_mix = y
        else:
            y_mix = y_mix + y

    # Save the mixed audio to file
    output_path = os.path.join(output_dir, 'mix{}.wav'.format(audio_idx+1))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if os.path.isfile(output_path):
        os.remove(output_path)
    sf.write(output_path, y_mix, sr)

print('Mixing completed successfully!')


