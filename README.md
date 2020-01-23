Speech to Text![Terminal Screenshot](/home/saurabh/Program/Projects/audio-recognition/terminal.png)

1.  Converts Speech to text using Google language API.

2.  Requirements 

    -   #### **ffmpeg**

        -   for audio format convertion to "wav" format

        -   ```bash
            sudo apt install ffmpeg
            ```

    -   #### Pip

        -   For python packages

        -   ```bash
            sudo apt install python3-pip
            ```

    -   ##### pydub

        -   Calls the ffmeg to convert audio files

        -   ```bash
            sudo pip3 install pydub
            ```

    -   SpeechRecognition

        -   Contains APIs for audio to text conversion

        -   ```bash
            sudo pip3 install SpeechRecognition
            ```

            

##### Usage

```bash
python3.6 transcribe.py audio_file_name
```

Ex

```bash
python3.6 transcribe.py transcript.mp3
```



Sample Output

