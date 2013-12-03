A very simple gimp plugin to upload the current image anonymously to imgur.

I created this because I was tired of the seemingly needless steps of exporting the image, and then finding it again in a file browser, when all I really wanted to do was share what I was working on quickly.

Install
-------
Simply copy whichever files you want into your GIMP plug-in directoy.  Normally located in \<GIMP Install\>/lib/gimp/2.0/plug-ins  Some systems will also have a ~/.gimp/plug-ins directory.

Make sure that the files are executable.


Usage
-----
Entries will be added to the filter menu under the Imgur heading.  Both will create a temporary file in your systems temporary directory and then upload that .png directly to imgur.  After which your default web browser should open a new tab with the image in it.

There is no support for deleting the image currently.

Note that the flatten and upload will flatten your image as part of the upload, however this will register as a normal operation and can be undone safely.
