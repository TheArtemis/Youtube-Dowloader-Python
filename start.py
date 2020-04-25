import os, sys
from pytube import YouTube


with open('songs.txt', 'r') as list:
    dw_list = [line.strip() for line in list]

def download(link):
    global name

    video = YouTube(link)

    path = os.path.join(os.getcwd(),'downloads')

    stream = video.streams.filter(only_audio=True).first()

    stream.download(path)

    name = video.title

def down_list():
    for i in dw_list:
        download(i)
        print(name + ' has been downloaded')
    return print('All downloads have been completed')

def down_sf():
    print("Insert link here:")
    link = input("")
    download(link)
    return print(name + ' has been downloaded')


def Benvenuto():
    print("[ 0 ] Download List")
    print("[ 1 ] Download Single File")
    risposta1 = input('')
    if int(risposta1) == 0:
        down_list()
    elif int(risposta1) == 1:
        down_sf()

def aElse():
    while True:
        print ("""
         >>>  Download another song?  <<<
        """)
        print ('''
            [ 0 ] yes   |   [ 1 ] no
        ''')
        again = input('')
        if int(again) == 0:
            down_sf()
        elif int(again) == 1:
            sys.exit(0)

Benvenuto()
aElse()
