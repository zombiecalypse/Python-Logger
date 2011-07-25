#!/usr/bin/python

# Filename: Logging.py
# Author:   Aaron Karper
# Created:  2011-07-21
# Description:
#          Provides a logging utility that can be silenced if necessary 
import sys,contextlib, collections


class Context(object):
	pass
class Fatal(Context):
	pass
class Error(Fatal):
	pass
class Warn(Error):
	pass
class Log(Warn):
	pass
class Debug(Log):
	pass

class Logger(object):
	def __init__(self, parent, context):
		self.__parent = parent
		self.__context = context
	def __call__(self, string):
		if issubclass(self.__parent.context,self.__context):
			self.__parent.show(string, self.__context)

def noinfo():
	return ""
class LoggerParent(object):
	def __init__(self, context = Warn, writable = sys.stdout, callable = noinfo):
		self.__writable = writable
		self._context = context
		self.padding = 10
		self.indent = collections.defaultdict(int)
		self.info_gen = callable
		self.info_padding = 0
	def get_context(self):
		return self._context
	def set_context(self,arg):
		assert issubclass(arg,Context)
		self._context = arg
	context = property(get_context, set_context)
	def __call__(self, context):
		return Logger(self, context)
	def show(self, string, context):
		self.__writable.write("%s%s%s\n" % (context.__name__.ljust(self.padding+self.indent[context]), str(self.info_gen()).ljust(self.info_padding), string))
default_logger = LoggerParent()
fatal = default_logger(Fatal)
error = default_logger(Error)
warn  = default_logger(Warn)
log   = default_logger(Log)
debug = default_logger(Debug)

@contextlib.contextmanager
def Indent(context = Log, logger = default_logger, ind = 2):
	logger.indent[context] += ind
	try:
		yield
	finally:
		logger.indent[context] -= ind
