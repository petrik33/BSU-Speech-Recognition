from scipy.io import wavfile
from scipy import signal
import numpy as np

rate, audio_data = wavfile.read("recorded_audio.wav")

cutoff = 6000
filtered_audio = signal.lfilter(*signal.butter(5, cutoff, fs=rate), audio_data)

wavfile.write("filtered_audio.wav", rate, filtered_audio.astype(np.int16))
