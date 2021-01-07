import pafy

url = input('Enter the url : ')

video = pafy.new(url)

audiostreams = video.audiostreams
f=0
for i in audiostreams:
    print(i.bitrate, i.extension, i.get_filesize())
    f = f+1
audiostreams[f-1].download()