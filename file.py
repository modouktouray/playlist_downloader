from pytube import Playlist
p = Playlist('https://www.youtube.com/watch?v=iHHBb-9455s&list=PLKpfEl4N7tRqIx4VZmuZBnUQ6vG4uDgq7')

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()








