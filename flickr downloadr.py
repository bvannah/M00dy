import flickrapi
import requests
import shutil
from PIL import Image

# Flickr api access key 
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)


keyword = input("Mood? ")

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

for i, photo in enumerate(photos):
    url = photo.get('url_c')
    if(url==None):
      continue
    print(url)
    resp = requests.get(url, stream=True)
    filepath="flickr pics/"+str(i)+".jpg"
    local_file=open(filepath, "wb+")
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Co  py the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp
    local_file.close()
    # Resize the image and overwrite it
    image = Image.open(filepath) 
    image = image.resize((256, 256), Image.ANTIALIAS)
    image.save(filepath)

    # get 50 urls
    if i > 50:
        break
