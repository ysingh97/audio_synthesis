from record_sound import *
import os
import numpy as np
import matplotlib.pyplot as plt
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
from IPython.display import Audio


recorder = AudioRecorder()
recorder.record()

# fname = "recording.wav"
# sr = 16000
# audio = utils.load_audio(fname, sample_length=40000, sr=sr)
# sample_length = audio.shape[0]
# print('{} samples, {} seconds'.format(sample_length, sample_length / float(sr)))




