import subprocess
import streamlit as st
import speech_recognition as sr
import os


st.write("# Video Captioning")

rawfile = st.file_uploader("Upload the file:")


if rawfile is not None:

    with st.spinner("Extracting the data!"):


        video_path = "videoplayback.mp4"

        with open(video_path, 'wb') as outputfile:
            outputfile.write(rawfile.getvalue())


        audio_path = video_path[:-4]+".wav"

        command = f'ffmpeg -i "{video_path}" -y -ab  160k -ac 2 -ar 44100 -vn "{audio_path}"'
        subprocess.call(command, shell=True)

        r = sr.Recognizer()

        with sr.AudioFile(audio_path) as source:
            audio = r.record(source, duration=100)

        text = r.recognize_google(audio, language = 'en-IN', show_all = True)

        # with open(f"{video_path[:-4]}.txt","w") as outputfile:
            # outputfile.write(text['alterative'][''])

        st.write("### Here's the transcript:")

        st.write(text['alternative'][0]['transcript'])

        st.success("Done!")

        rawfile = None




    # open(f"{video_path[:-4]}.txt", "w").write(str(text))