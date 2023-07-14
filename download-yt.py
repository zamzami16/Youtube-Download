# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:08:14 2022

@author: yusuf
"""

import os
import moviepy.editor as mp
import datetime
from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
from multiprocessing import Process


mp4_path_exist = []
for file in os.listdir(os.path.join(os.getcwd(), "videos")):
    mp4_path_exist.append(file)

success_download = []
failed_download = []
already_downloaded = []


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def getPlaylist():
    playlists = [
        # "https://www.youtube.com/watch?v=GqQcqQxFXBM",
    ]
    urls = [
        # "https://www.youtube.com/playlist?list=PLDsQg9WjiOwt6HbI7dhp_Thjh454fda4H",
        # "https://www.youtube.com/playlist?list=PLPZNgkDcsPLJmUbPehaAQeN3mHc0jHxND",
        # "https://www.youtube.com/playlist?list=PLY5mXGIp5tYVEeteiGGLbgVy9f5pgNNjq",
        # "https://www.youtube.com/playlist?list=PLf3ktCjTDhNEoetDx_9FVBkLlivGgQ7tn",
        # "https://www.youtube.com/playlist?list=PL0BD69368AB943C89",
        # "https://www.youtube.com/playlist?list=PLu1S36l0eVs3IS5tPhqnfeuWs0LhpmkMR",
        # "https://www.youtube.com/playlist?list=PLu1S36l0eVs3uxzUk38MiXL9PMRhlB2-w",
    ]
    with open("urls.txt") as f:
        for url in f.readlines():
            if url.startswith("http"):
                urls.append(url)

    for url in urls:
        playlists.extend(Playlist(url))

    return playlists


def convert_(base_folder, target, mp4_path):
    mp3_path = os.path.join(base_folder, target)
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path, verbose=False)


def downloads(url, idx, size, convert, base_folder=os.getcwd()):
    attemp = 1
    try:
        yt = YouTube(url)

    except VideoUnavailable:
        print(f"Video {url} is unavaialable, skipping.")
    else:
        print(f"{idx} from {size}\t|\tDownloading {yt.title}")
        while attemp < 2:
            try:
                # get file name
                mp4_path_new = yt.title + ".mp4"
                # print(mp4_path_new)
                if mp4_path_new not in mp4_path_exist:
                    mp4_path = (
                        yt.streams.filter(only_audio=True)
                        .first()
                        .download(os.path.join(base_folder, "videos"))
                    )
                    print(f"Downloaded!\t|{idx} from {size}|\t{yt.title}")
                    success_download.append(
                        f"Downloaded!\t|{idx} from {size}|\t{yt.title}"
                    )
                    if convert:
                        convert_(
                            os.path.join(base_folder, "audio"),
                            os.path.splitext(yt.title)[0] + ".mp3",
                            mp4_path,
                        )

                    attemp += 2
                else:
                    print(
                        f"Already Downloaded!\t|{idx} from {size}|\t{yt.title}"
                    )
                    already_downloaded.append(
                        f"Already Downloaded!\t|{idx} from {size}|\t{yt.title}"
                    )
                    attemp += 2
            except:
                # print("error, skipping the file")
                attemp += 1
                print(
                    f"{idx} from {size}\t{yt.title} \tDownload Failed, try downloading again!\n"
                )
                failed_download.append(
                    f"{idx} from {size}\t{yt.title} \tDownload Failed, try downloading again!"
                )


def main_(n_chunk, convert=True):
    idx = 0
    all_playlist = getPlaylist()
    size = len(all_playlist)
    for playlists in chunks(all_playlist, n_chunk):
        process = []
        for url in playlists:
            idx += 1
            p = Process(target=downloads, args=(url, idx, size, convert))
            process.append(p)
            p.start()

        for p in process:
            p.join()
    return ""


if __name__ == "__main__":
    if os.path.exists("urls.txt"):
        n_chunk = 5
        main_(n_chunk)
        name = rf"reports_{datetime.datetime.now().__str__()}_.txt"
        with open(name) as f:
            for success in success_download:
                f.writelines(success)
            for failed in failed_download:
                f.writelines(failed)
            for already in already_downloaded:
                f.writelines(already)

        print("Download complete...")
        print(f"Success Download: \t{success_download.count()}")
        print(f"Failed DOwnload: \t{failed_download.count()}")
        print(f"Already Downloaded: \t{already_downloaded.count()}")
        print(f"Summary file in: {name}")
    else:
        print("Files 'urls.txt' doesn't exists.")
