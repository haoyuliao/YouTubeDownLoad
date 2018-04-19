import pytube
link = "https://www.youtube.com/watch?v=5mUV6lTmyq4&index=18&list=PLBkfOXPAnKmjjjUpMw4mde9AaRrAQKlbh"
yt = pytube.YouTube(link)
stream = yt.streams.first()
print(stream)
stream.download()
