from pytube import Playlist
p = Playlist('https://www.youtube.com/watch?v=qP8ZVhYt1og&list=RDCMUCgOoP5NSZ1HA5dgJg2I8k0A&start_radio=1&rv=qP8ZVhYt1og')

print(f'Downloading : {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()








