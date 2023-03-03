# import required libraries
from pydub import AudioSegment
from pydub.playback import play
import os
import glob


'''
// ----------Creation fo mixed audio files from two different source folder----------//
'''
audio_files1 = glob.glob("audio/bulldozer_wav/*.wav")
audio_files2 = glob.glob("audio/dump_truck_wav/*.wav")

output_folder = "audio\output"


audios = []
for i in range(len(audio_files1)):
    audio1 = AudioSegment.from_file(audio_files1[i])
    audio2 = AudioSegment.from_file(audio_files2[i])
    mixed_audio = audio1.overlay(audio2)
    audios.append(mixed_audio)

print(len(audios))


for i in range(len(audios)):
    filename = os.path.splitext(os.path.basename(audio_files1[i]))[0][0:9] + "_" + os.path.splitext(os.path.basename(audio_files2[i]))[0] + ".wav"
    output_path = os.path.join(output_folder, filename)
    print(output_path)
    audios[i].export(output_path, format="wav")


'''
// ------------Basic function of the extracting the basic information of about any audio files--------------//
'''

# Check the all information of any audio files
def audio_info(audio_file):
    # Check some information of the trucks
    wav_file = AudioSegment.from_file(audio_file)
    # data type for the file
    print(f"a. Type of the file: {type(wav_file)}")
    #  To find frame rate of song/file
    print(f"b. Frame rate of the file: {wav_file.frame_rate}")
    # To know about channels of file
    print(f"c. Channel of the file: {wav_file.channels}")
    # Find the number of bytes per sample
    print(f"d. Bytes per sample of the file: {wav_file.sample_width}")
    # Find Maximum amplitude
    print(f"e. Maximum amplitude of the file: {wav_file.max}")
    # To know length of audio file
    print(f"f. Total length of the file: {len(wav_file)}")


# Let's check our files
bull = (r"C:\Users\user\Documents\DeepLearning\JupyterNoteBook\Feature Extraction\audio\bulldozer_wav\bulldozer_5sec_002.wav")
dump = (r"C:\Users\user\Documents\DeepLearning\JupyterNoteBook\Feature Extraction\audio\dump_truck_wav\dump_truck_5sec_001.wav")
mixed = (r"C:\Users\user\Documents\DeepLearning\JupyterNoteBook\Feature Extraction\audio\output\bulldozer_dump_truck_5sec_001.wav")

audio_info(bull)
audio_info(dump)
audio_info(mixed)