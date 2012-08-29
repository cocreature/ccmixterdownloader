#!/usr/bin/python3

import urllib.request
import sys

artist = sys.argv[1]
outputfile = sys.argv[2]

offset = 0
downloadlinks = ""
fileHandle = open (outputfile, 'w')

while (downloadlinks != "file not found"):
    try:
        downloadlinks = urllib.request.urlopen("http://ccmixter.org/api/query?user=" + artist + "&f=m3u&offset=" + str(offset)).readlines()
    except urllib.error.HTTPError:
        print ("Finished")
        break
    for downloadlink in downloadlinks:
        fileHandle.write(downloadlink.decode('utf-8'))
    offset += 200
fileHandle.close()
