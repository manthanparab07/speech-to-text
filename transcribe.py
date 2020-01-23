import speech_recognition as sr
from os import path
from pydub import AudioSegment
import sys
import csv

# Check for filename in argument
if len(sys.argv) <= 1:
    print("Audio File Not provided!!\n Exiting...")
    sys.exit(1)

# Check for filename and fileExtension

filename = sys.argv[1]
fileExtension = filename.split('.')[-1]

print("File Name : ", filename)
print("File Type : ", fileExtension)

print("Audio Conversion to wav format")
# Convert the audio file into wav format
sound = AudioSegment.from_file(filename, fileExtension)
sound.export("transcript.wav", format="wav")

print("Conversion Complete  !")
print("Converting into text :")

# transcribe audio file
AUDIO_FILE = "transcript.wav"

textForm = None

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
    textForm = r.recognize_google(audio)
    # print("Transcription: " + r.recognize_google(audio))

print("Converted !!")
print(textForm)

print("Saving into File")

file_desc = open(filename.split(".")[0] + ".txt", "w")
file_desc.write(textForm)

# uncomment for saving in csv
'''

with open("transcript.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(textForm)

'''
