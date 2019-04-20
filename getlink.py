from pprint import pprint as print
from pytube import YouTube
import requests,re,os
links = set(re.findall(r'href="/watch\?(.*?)"', requests.get('https://www.youtube.com/playlist?list=PLHuVrfp6F2wVBXJR-yDFTbwFqxPZA8x-I').text));
i = 1
for link in links:
	link = "https://youtube.com/watch?" + link.split('&amp;')[0]
	print(link + ' | video: --> ' + str(i))
	i += 1
	yt = YouTube(link)
	#yt = yt.get('mp4', '720p')
	yt = yt.streams.filter(progressive=True, file_extension='mp4').first()
	if not os.path.exists('./download'): os.makedirs('./download')
	yt.download('./download')
print('-----------------------------end-------------------------------')