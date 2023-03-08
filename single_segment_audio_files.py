import librosa
import os
import soundfile as sf

# Set the directory paths for input and output
input_dir = "2_Bulldozer_wav"
output_dir = "Bulldozer_5Sec"

# Define the duration of the audio segments in seconds
segment_duration = 5

# Loop through all audio files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".wav"): # check if the file is a wav file
        audio_path = os.path.join(input_dir, filename)
        y, sr = librosa.load(audio_path, sr=None) # load audio file
        segment_length = sr * segment_duration # calculate the length of the audio segment in samples
        n_segments = len(y) // segment_length # calculate the number of segments in the audio file
        for i in range(n_segments):
            start = i * segment_length # calculate the start time of the segment
            end = (i + 1) * segment_length # calculate the end time of the segment
            segment = y[start:end] # extract the audio segment
            name = os.path.splitext(filename)[0]
            # segment_path = os.path.join(output_dir, f"{filename}_{i+1}.wav") # create the path for the segmented audio file
            segment_path = os.path.join(output_dir, f"{name}_{i+1}.wav") # create the path for the segmented audio file
            sf.write(segment_path, segment, sr) # save the segmented audio file

