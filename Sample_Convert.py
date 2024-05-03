# This is a sample of a program that converts cold fusion into a SCORM file

import os
from pathlib import Path
from mutagen.mp3 import MP3


# function creates a list of images in the folder
def get_images(f_path):
    try:
        image_names = []
        for file in os.listdir(f_path):
            if file.endswith(".jpg")
                # Add the file name to the list
                res = file.replace('.jpg', '')
                image_names.append(res)
            elif file.endswith(".png"):
                res = file.replace('.png', '')
                image_names.append(res)
            elif file.endswith("jpeg"):
                res = file.replace('.jpeg', '')
                image_names.append(res)
        return image_names
    except:
        RuntimeError("unable to handle error")

# function creates a list of audio files in the folder
def get_media(f_path):
    try:
        media_names = []
        for file in os.listdir(f_path):
            if file.endswith(".mp3"):
                media_names.append(file)
        return media_names
    except:
        RuntimeError("unable to handle error")


# This funtion adds html tags to the beginning of the .cfm file
def prepend_html(f_path, f_pre_html):
    try:
        cfm_list = os.listdir(f_path)
        for i in cfm_list:
            with open(f_path + "//" + i, 'r+', encoding="UTF-8") as f:
                f_data = f.read()
                html_p = '\n'.join(f_pre_html)
                f.seek(0, 0)
                f.write(html_p + f_data)
                f.close()
    except UnicodeDecodeError as e:
        print(e)


# function changes the files from .cfm to .html
def change_extension(f_path):
    try:
        for file in os.listdir(f_path):
            path = Path(f_path + '//' + file)
            new_extension = path.with_suffix(".html")
            path.rename(new_extension)
    except:
        RuntimeError("unable to handle error")

# function calculates the length of the audio files
def audio_length(a_path, media_names):
    try:
        all_length = []
        for i in media_names:
            audio = MP3(a_path + '//' + i)
            audio_time = audio.info.length
            x = round(audio_time * .60)
            all_length.append(i + ' = ' + str(x))
        f = open(a_path + '//' + 'audio_length.txt', 'w')
        for item in all_length:
            f.write(item + "\n")
        f.close()
    except:
        return None

    # ....
