# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:55:49 2022

@author: yusuf
"""

import os
import re
import moviepy.editor as mp

base_folder = os.getcwd()
folder = os.path.join(base_folder, "videos")
for file in os.listdir(folder):
    if re.search("mp4", file):
        mp4_path = os.path.join(folder, file)
        mp3_path = os.path.join(
            os.path.join(base_folder, "audio"),
            os.path.splitext(file)[0] + ".mp3",
        )
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
