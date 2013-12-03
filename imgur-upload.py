#!/usr/bin/env python

#   Copyright 2013 Joseph Utecht
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

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
    "Open source (GPLv3)",
    "2013",
    "<Image>/Filters/Imgur/Upload Current Layer",
    "*",
    [],
    [],
    upload_to_imgur)

main()
