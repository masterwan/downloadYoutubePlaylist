from pprint import pprint as print
from pytube import YouTube
import requests,re,os
links = set(re.findall(r'href="/watch\?(.*?)"', requests.get(input('playlist youtube link:')).text));

def dlYoutube(link, path):
	yt = YouTube(link)
	#yt = yt.get('mp4', '720p')
	yt = yt.streams.filter(progressive=True, file_extension='mp4').first()
	if not os.path.exists(path): os.makedirs(path)
	yt.download(path)
	print('--*< - success - >*--')	

i = 1
path = './download'
for link in links:
	link = "https://youtube.com/watch?" + link.split('&amp;')[0]
	print(link + ' | video: --> ' + str(i))
	i += 1
	try:
		dlYoutube(link, path)
	except:
		try:
			print('attempt 2')
			dlYoutube(link, path)
		except:
			try:
				print('attempt 3')
				dlYoutube(link, path)	
			except:
				print('this video is not available')

print('-----------------------------end-------------------------------')