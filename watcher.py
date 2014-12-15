#! /usr/bin/python

# Author: Abid H. Mujtaba
# Date: 2014-12-15

# Source: http://www.saltycrane.com/blog/2010/04/monitoring-filesystem-python-and-pyinotify/

# This script uses the pyinotify library which in turn uses the Linux kernel's inotify facility to detect filesystem changes and take appropriate actions.

import pyinotify

# Import the flags that we will use to monitor events in the specified folder
IN_CLOSE_WRITE = pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_CLOSE_WRITE']
IN_CLOSE_NOWRITE = pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_CLOSE_NOWRITE']

# Perform a bitwise OR operation to construct a combined set of flags
MONITOR_FLAGS = IN_CLOSE_WRITE | IN_CLOSE_NOWRITE

# We specify the folders that need to be monitored
MONITOR_FOLDERS = ['/home/abid/Documents/workspace/.misc',
                   '/home/abid/Pictures/.Personal']


class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_ACCESS(self, event):
        print "ACCESS event:", event.pathname

    def process_IN_ATTRIB(self, event):
        print "ATTRIB event:", event.pathname

    def process_IN_CLOSE_NOWRITE(self, event):
        print "CLOSE_NOWRITE event:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        print "CLOSE_WRITE event:", event.pathname

    def process_IN_CREATE(self, event):
        print "CREATE event:", event.pathname

    def process_IN_DELETE(self, event):
        print "DELETE event:", event.pathname

    def process_IN_MODIFY(self, event):
        print "MODIFY event:", event.pathname

    def process_IN_OPEN(self, event):
        print "OPEN event:", event.pathname

def main():
    # watch manager
    wm = pyinotify.WatchManager()

    for folder in MONITOR_FOLDERS:

        wm.add_watch(folder, MONITOR_FLAGS, rec=True)

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()