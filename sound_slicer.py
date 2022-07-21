import argparse
import os
import librosa
import numpy as np
from soundfile import write

# Create parser and add arguments for path, name, start point, sample rate, and length.
parser = argparse.ArgumentParser(description="Slice sounds into usable sizes. Requires the path to the file, samplerate, and length in seconds. Will be saved in slices folder.")
parser.add_argument('-p', '--path', help='Path to the audio file you wish to slice.', type=str, required=True)
parser.add_argument('-n', '--name', help='Name of new sound slice.', type=str, required=True)
parser.add_argument('-st', help='Start point of the sample of the file', type=int, required=False)
parser.add_argument('-sam', help='Samplerate of the audio file.', type=int, required=True)
parser.add_argument('-len', help='Length of the slice in seconds', type=int, required=True)

args = parser.parse_args()

# Check to make sure that directory for final slices exists and if it does not, create it.
if not os.path.isdir('slices/'):
    os.mkdir('slices/')

# Load song
song, _ = librosa.load(path = args.path, sr=args.sam)

# If start point has not been specified, generate random start point.
if args.st == None:
    start = np.random.choice(song.shape[0])
else:
    start = args.st

# Generate end point based on start point, sample rate, and length of slice.
end = start + args.sam * args.len

# Write to a file
write(file = f'slices/{args.name}.wav', data=song[start:end], samplerate=args.sam)
