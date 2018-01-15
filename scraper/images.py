from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os

def search():
    search = raw_input("Search for: ")
    params = {"q": search}
    r = requests.get("http://www.bing.com/images/search", params=params)
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
       os.makedirs(dir_name)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("URL: " + str(item.attrs["href"]))
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./scraped_images/" + title, img.format)
            except:
                print("Could not save image.")
        except:
            print("Could not request image.")

while True:
    search()
