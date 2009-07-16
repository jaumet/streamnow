STREAMNOW
---------

Very simplent fronend to gstreamer to get your webcam streaming to an icecast server.

DEPENDENCIES:
------------
- Gstreamer -> gst-launch-0.10 [JAY, we are using this gst-launch]
- python
- GTK
- oggfwd


INSTALL
-------
JAY, right now you must do:
$: cd /path_to_streamnow/
$: ./streamnow-config.py

JAY, in gnome/ you have:
	- streamnow.desktop: his must go in /usr/share/applications/streamnow.desktop
	- In images/ you have all the versions of the streamnow icon. Must go to  

YOU NEED AN ACCOUT IN AN ICECAST SERVER
---------------------------------------
You need to have an accessible icecast server. If you are streaming free, non-commercial contents, we recommend to register a channel fro free in http://giss.tv

CHANGELOG
---------
- 1.0 Vienna july 2009

LICENSE
-------
GPL, v3

CREDITS
-------
Jaume Nualart [jaume AT nualart.cat]
Chris Hager [chris AT linuxuser.at]
Anna Sala [asalavila AT gmail.com]
Jay Vaughan [jayv AT synth.net]


