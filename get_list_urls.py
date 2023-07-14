import requests
from pprint import pprint
from bs4 import BeautifulSoup
from pytube import YouTube, Playlist

p = Playlist("https://www.youtube.com/watch?v=WlmWXoP0C0s&list=RDWlmWXoP0C0s&index=2")
for pp in p:
    print(pp)

# resp = requests.get("https://www.youtube.com/watch?v=WlmWXoP0C0s&list=RDWlmWXoP0C0s")
# # print(resp.text)
# page = resp.text
# soup = BeautifulSoup(page, "html.parser")
# res = soup.find_all(id='playlist_items')
# for l in res:
#     print(l.get("href"))


# <a id="wc-endpoint" class="yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer" href="/watch?v=ycc60Ymh_F0&list=RDEMraOQKiYpaIJU54QI6FWxmQ&index=1">