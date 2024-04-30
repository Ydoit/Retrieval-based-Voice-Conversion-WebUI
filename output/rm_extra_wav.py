import os
import random

# Get all .wav files in the current directory
wav_files = [f for f in os.listdir(".") if f.endswith(".wav")]

# Randomly select 10 files to keep
to_keep = random.sample(wav_files, 10)

# Rename the files to keep
for i, filename in enumerate(to_keep, start=1):
    os.rename(filename, f"audio{i}.wav")

# Delete the rest of the files
for filename in wav_files:
    if filename not in to_keep:
        os.remove(filename)
