#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade

from os import system as executecmd
import os.path

_sizes = ["160x120", "240x180", "256x192", "320x240", "384x288", "480x360"]
_fps = ["1", "3", "5", "8", "10", "12", "15", "25"]

class StreamConf:
    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.xml = gtk.glade.XML("gui.glade")
        self.window = self.xml.get_widget("StreamNow Configuration")
        self.window.connect("destroy", self.destroy)
        
        button_bye = self.xml.get_widget("button2")
        button_bye.connect_object("clicked", gtk.Widget.destroy, self.window) 
        
        button_apply = self.xml.get_widget("button1")
        button_apply.connect("clicked", self.apply) 

        button_open = self.xml.get_widget("button3")
        button_open.connect("clicked", self.openconf) 

        button_stream = self.xml.get_widget("button4")
        button_stream.connect("clicked", self.startstream) 

        button_ff = self.xml.get_widget("button5")
        button_ff.connect("clicked", self.startff) 
        button_ff.set_sensitive(False)

        # Bind Window Elements
        self.wTitle =  self.xml.get_widget("entry1")
        self.wServer =  self.xml.get_widget("entry2")
        self.wPort =  self.xml.get_widget("entry3")
        self.wPasswd =  self.xml.get_widget("entry4")
        self.wMountpoint =  self.xml.get_widget("entry5")
        self.wSize =  self.xml.get_widget("combobox1")
        self.wFPS =  self.xml.get_widget("combobox2")        
        
        # Default Values
        self.wSize.set_active(1)
        self.wFPS.set_active(5)
        
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

    def apply(self, sender):
        title = self.wTitle.get_text()
        server = self.wServer.get_text()
        port = self.wPort.get_text()
        passwd = self.wPasswd.get_text()
        mountpoint = self.wMountpoint.get_text()
        size = self.wSize.get_active_text()
        fps = self.wFPS.get_active_text()

        # filechooser = self.xml.get_widget("fileselection1")
        # filechooser.show()
        chooser = gtk.FileChooserDialog("Save Configuration as",action=gtk.FILE_CHOOSER_ACTION_SAVE,
                               buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
        res = chooser.run()
        fn = chooser.get_filename()
        chooser.destroy()
        
        if not fn:
            print "Cancel Saving"
            return
            
        print "Saving To File:", fn
        
        f = open(fn, "w")
        f.write("title = %s\n" % title)
        f.write("server = %s\n" % server)
        f.write("port = %s\n" % port)
        f.write("passwd = %s\n" % passwd)
        f.write("mountpoint = %s\n" % mountpoint)
        f.write("size = %s\n" % size)
        f.write("fps = %s\n" % fps)
        f.close()

        button = self.xml.get_widget("button4")
        button.set_sensitive(True)
                
        print "Configuration Saved"
        
    def openconf(self, sender):
        chooser = gtk.FileChooserDialog("Open Configuration File",action=gtk.FILE_CHOOSER_ACTION_OPEN,
                               buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        res = chooser.run()
        fn = chooser.get_filename()
        chooser.destroy()
        
        if not fn:
            print "Cancelled"
            return
            
        print "Loading:", fn
        if not os.path.isfile(fn):
            print "File not found"
            return 
        
        # Get Configuration Dict from the File
        conf = self.readconf(fn)
        
        self.wTitle.set_text(conf["title"])
        self.wServer.set_text(conf["server"]) 
        self.wPort.set_text(conf["port"])
        self.wPasswd.set_text(conf["passwd"])
        self.wMountpoint.set_text(conf["mountpoint"])
        self.wSize.set_active(_sizes.index(conf["size"].replace(" ", "")))
        self.wFPS.set_active(_fps.index(conf["fps"]))


        button = self.xml.get_widget("button4")
        button.set_sensitive(True)
        
    def readconf(self, fn):
        # Read a config file to a Dict
        f = open(fn)
        conf_str = f.read()
        f.close()
        
        conf_arr = conf_str.split('\n')
        conf_dict = {}
        
        for c in conf_arr:
            c = c.strip()
            if not c:
                # empty line
                continue
                
            if c[:1] == '#':
                # comment
                continue
                
            (arg, data) = c.split("=")
            conf_dict[arg.strip().lower()] = data.strip()
            
        return conf_dict
        
    def startstream(self, sender):
        # Assembling the Command and Starting the Stream in a Console
        title = self.wTitle.get_text()
        server = self.wServer.get_text()         #
        port = self.wPort.get_text()             #
        passwd = self.wPasswd.get_text()         #
        mountpoint = self.wMountpoint.get_text() #
        fps = self.wFPS.get_active_text()        #
        size = self.wSize.get_active_text()      #
        (w, h) = size.split("x")
        
        sender.set_sensitive(False)
        
        cmd = "gst-launch-0.10 v4l2src ! queue ! videorate ! video/x-raw-yuv, framerate=%s/1 ! videoscale ! video/x-raw-yuv,width=%s,height=%s ! ffmpegcolorspace ! theoraenc quality=8 ! queue ! oggmux name=mux  alsasrc ! audio/x-raw-int,rate=22050,channels=1,depth=16 ! queue ! audioconvert ! vorbisenc ! queue ! mux. mux. ! fdsink | oggfwd %s %s %s /%s &" % (fps, w.strip(), h.strip(), server, port, passwd, mountpoint)
        executecmd(cmd)        
        button_ff = self.xml.get_widget("button5")
        button_ff.set_sensitive(True)

    def startff(self, sender):
        server = self.wServer.get_text()         #
        port = self.wPort.get_text()             #
        mountpoint = self.wMountpoint.get_text() #
        executecmd("firefox http://%s:%s/%s" % (server, port, mountpoint))

if __name__ == "__main__":
    win = StreamConf()
    win.main()
    
