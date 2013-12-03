#!/usr/bin/env python

from gimpfu import *
import os
import json
import tempfile
import urllib
import urllib2
import webbrowser
from base64 import b64encode


def upload_to_imgur(image, layer):
    ''' Save the current layer into a PNG file, and then uploads to imgur. 
    
    Parameters:
    image : image The current image.
    layer : layer The layer of the image that is selected.
    '''

    api_key = 'c4622163d7339fe'
    headers = {"Authorization": "Client-ID {}".format(api_key)}
    url = "https://api.imgur.com/3/upload.json"

    # Indicates that the process has started.
    gimp.progress_init("Uploading to imgur...")
    
    try:
        # Save as PNG
        outputFolder = tempfile.gettempdir()
        f = os.path.join(outputFolder, layer.name + ".png")
        gimp.pdb.file_png_save(image, layer, f, "raw_filename", 0, 9, 0, 0, 0, 0, 0)
        data = urllib.urlencode({
                'key': api_key, 
                'image': b64encode(open(f, 'rb').read()),
                'type': 'base64',
                'name': f,
                'title': 'Picture no. 1'
            })
        r = urllib2.Request(url, data, headers)
        response = json.loads(urllib2.urlopen(r).read())
        if(response['success']):
            webbrowser.open(response['data']['link'])
        else:
            gimp.message(j1)
    except Exception as err:
        gimp.message("Unexpected error: " + str(err))
    
register(
    "imgur-upload",
    "Upload the current image to imgur",
    "Save the current layer into a PNG file, and then upload to imgur.",
    "JRU",
    "Open source (BSD 3-clause license)",
    "2013",
    "<Image>/Filters/Imgur/Upload Current Layer",
    "*",
    [],
    [],
    upload_to_imgur)

main()
