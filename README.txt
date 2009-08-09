STREAMNOW
---------

Very simplent fronend to gstreamer to get your webcam streaming to an icecast server.

DEPENDENCIES:
------------
- python
- Gstreamer -> gst-launch-0.10 [JAY, we are using this gst-launch]
- GTK
- oggfwd

RUN IT
------
	$: cd /path_to_streamnow/
	$: ./streamnow

INSTALL
-------
	- streamnow.desktop: his must go in /usr/share/applications/streamnow.desktop

	sudo cp GNOME/streamnow.desktop /usr/share/applications/streamnow.desktop

	- In GNOME/icons/ you'll find all the versions of the streamnow icons:

		For easy peacy 1.1: cp the icons in all this directories with the name 
		streamnow.png in the respective size folder
		
		/usr/share/icons/easypeasy/16x16/apps/streamnow.png
		/usr/share/icons/easypeasy/22x22/apps/streamnow.png
		/usr/share/icons/easypeasy/24x24/apps/streamnow.png
		/usr/share/icons/easypeasy/32x32/apps/streamnow.png
		/usr/share/icons/gnome-brave/16x16/apps/streamnow.png
		/usr/share/icons/gnome-brave/22x22/apps/streamnow.png
		/usr/share/icons/gnome-brave/24x24/apps/streamnow.png
		/usr/share/icons/gnome-brave/32x32/apps/streamnow.png
		/usr/share/icons/hicolor/16x16/apps/streamnow.png
		/usr/share/icons/hicolor/22x22/apps/streamnow.png
		/usr/share/icons/hicolor/24x24/apps/streamnow.png
		/usr/share/icons/hicolor/32x32/apps/streamnow.png
		/usr/share/icons/hicolor/48x48/apps/streamnow.png


YOU NEED AN ACCOUT IN AN ICECAST SERVER
---------------------------------------
You need to have an accessible icecast server. If you are streaming free, non-commercial contents, we recommend to register a channel for free in http://giss.tv

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
Jay Vaughan [jay AT synth.net]


