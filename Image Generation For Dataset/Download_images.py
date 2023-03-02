import requests

# Set the RA and Dec values
ra = '123.45'
dec = '67.89'

# Set the URL for the image
url = f'http://skyserver.sdss.org/dr15/SkyServerWS/ImgCutout/getjpeg?ra={ra}&dec={dec}&scale=0.4&width=512&height=512'

# Send a request to the URL and save the image
response = requests.get(url)
open('image.jpg', 'wb').write(response.content)
