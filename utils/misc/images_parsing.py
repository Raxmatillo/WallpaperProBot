import uuid
import requests
from bs4 import BeautifulSoup
import json



def images_list(text: str):
    URL = f"https://www.wallpaperflare.com/search?wallpaper={text}"
    r = requests.get(URL)


    soup = BeautifulSoup(r.content, 'html5lib')

    table = soup.find('ul', attrs={'id': 'gallery'})


    images = []

    for row in table.findAll('li', attrs={"itemprop":"associatedMedia"}):
        img_title = row.img["title"]
        img_url = row.a["href"]
        img_thumb = row.img["data-src"]
        images.append(
            {
                'id': f"{uuid.uuid1()}",
                'title': img_title,
                'img_thumb': img_thumb,
                'img_url': img_url
            }
        )


    return images




def link_image(url: str):
    URL = f"{url}/download"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    image = soup.find("img", attrs={"id": "show_img"})

    return image["src"]