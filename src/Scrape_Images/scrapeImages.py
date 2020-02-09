from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

def get_images(query):
    counter = 1
    url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"

    #add the directory for your image here
    DIR="Pokemon_Images/test"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)

    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("a",{"class":"iusc"}):
        #print a
        m = json.loads(a["m"])
        turl = m["turl"]
        murl = m["murl"]

        image_name = query + '_test_' + str(counter) + '.jpg'
        counter += 1
        #urllib.parse.urlsplit(murl).path.split("/")[-1]
        print(image_name)

        ActualImages.append((image_name, turl, murl))

    print("There are " , len(ActualImages),"images")

    if not os.path.exists(DIR):
        os.mkdir(DIR)

    query += "_test"
    DIR = os.path.join(DIR, query)
    if not os.path.exists(DIR):
        os.mkdir(DIR)

    ##print images
    for i, (image_name, turl, murl) in enumerate(ActualImages):
        try:
            raw_img = urllib.request.urlopen(turl).read()

            cntr = len([i for i in os.listdir(DIR) if image_name in i]) + 1

            f = open(os.path.join(DIR, image_name), 'wb')
            f.write(raw_img)
            f.close()
        except Exception as e:
            print("Could not load : " + image_name)
            print(e)

#Directory where pokemon names are stored
pokemonDir = "C:/Users/bryan/Documents/Carleton 19-20/Ottahack/UOttaHack-2020/src/Scrape_Images/Pokemon_Names/pokemon.txt"
file = open(pokemonDir)
pokemonNames = file.read()
pokemonNames = pokemonNames.split(",")
for name in pokemonNames:
    get_images(name)
print('ended succesfully')