# Python-Logging #

A context based logging utility for Python.

## Intro ##

When writing a bigger project, one comes to thing about textual output. In some
cases, such as tests, it should be avoided, but for debugging, it might be
important to have. Further, you might not want to be bothered with the
debugging output of another team members functions or from another module.
Hence Python-Logging provides you with a context based output, that can be used
to generate logfiles or print to the console and shuts up the logging you don't
need.

## Use ##

For your convenience, there are already predefined Contexts and loggers. Thus the easiest way to use Python-Logging is

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
    
However, you probably don't want to polute other peoples with your own
debugging output. So lets define a new Context:

    from Logging import *
    class MyModuleDebug(Debug):
        pass
    class OtherModuleDebug(Debug):
        pass
    debug = default_logger(MyModuleDebug)
    
    default_logger.padding = 20 # prettier
    
    default_logger.context = OtherModuleDebug # or just Debug
    debug("Does not print")
    default_logger.context = MyModuleDebug
    debug("Does print")

You might also add more information.

    from Logging import *
    from datetime import datetime
    default_logger.info_gen = datetime.now
    default_logger.info_padding = 30
    warn("Has time included")
