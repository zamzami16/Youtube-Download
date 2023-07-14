# Youtube Downloder

I use this script to download videos on youtube and convert it to `.mp3` file.

> Link on `urls.txt` can be `Playlist`, `Videos`

the output will be an audio file of the videos.
it use multi threading for 5 thread. if you want change the number of thread, you can modify it in `download-yt.py`

```python
if __name__ == "__main__":
    if os.path.exists("urls.txt"):
        n_chunk = 5 # Change this for number of thread you want.
```

## Whats Next

1. CLI for change the number of thread
2. For now, it still download videos and then convert it to `.mp3` file simultaniously using `moviepy`. _This approach will drop the perfomance while convert the video to audio_, I want improve to allow download first, and then convert all downloded video to audio file (`.mp3`).
3. GUI using pyqt5 or TKinter

## How to use

- Clone this repo
  ```bash
  git clone https://github.com/zamzami16/Youtube-Download.git
  ```
- Create environment
  ```bash
  cd Youtube-Download
  pip install -r requirements.txt
  ```
- Add youtube URL to `urls.txt`
- Run Scripts
  ```bash
  python download-yt.py
  ```
