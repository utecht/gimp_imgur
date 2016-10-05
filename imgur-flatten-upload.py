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
import json
import os
import tempfile
import urllib
import urllib2
import webbrowser
from base64 import b64encode


def upload_to_imgur(image, layer):
    ''' Flatten and then save as PNG file, and then uploads to imgur. 
    
    Parameters:
    image : image The current image.
    layer : the current layer
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
        gimp.pdb.file_png_save(image, image.flatten(), f, "raw_filename", 0, 9, 0, 0, 0, 0, 0)
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
    "imgur-flatten-upload",
    "Upload the current flattened image to imgur",
    "Flatten and then save as PNG file, and then uploads to imgur.",
    "JRU",
    "Open source (BSD 3-clause license)",
    "2013",
    "<Image>/Filters/Imgur/Flatten and Upload",
    "*",
    [],
    [],
    upload_to_imgur)

main()
