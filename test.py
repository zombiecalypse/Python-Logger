#!/usr/bin/python

# Filename: test.py
# Author:   Aaron Karper
# Created:  2011-07-21
# Description:
#          The examples from the README 


from Logging import *
# these do not print, because default context requires Warn or higher
debug("Some unimportant detail about the implementation %i" % 77)
log("Hello world") 
# these do print
warn("rainy weather")
error("OMG!")
fatal("ABORT SHIP!")

default_logger.context = Debug
# Now these will print
debug("Some unimportant detail about the implementation %i" % 77)
log("Hello world") 
print "==================================================================="
class MyModuleDebug(Debug):
		pass
class OtherModuleDebug(Debug):
		pass
debug = default_logger(MyModuleDebug)

default_logger.padding = 20 # prettier

default_logger.context = OtherModuleDebug 
debug("Does not print")
default_logger.context = Debug
debug("Does not print")
default_logger.context = MyModuleDebug
debug("Does print")
print "==================================================================="
from Logging import *
from datetime import datetime
default_logger.info_gen = datetime.now
default_logger.info_padding = 30
warn("Has time included")
