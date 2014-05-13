# Author Pei-Chen Tsai aka Hammer
# email : please use gitHub issue system
# To use : please pipe "make | python makeflt.py" as start

import os
import sys

global DB_FLT, DB_TAL
global FLT_MODE_ERROR_ONLY, FLT_MODE_WARNNING_ONLY, FLT_MODE_ALL
global FLT_MODE
global WARNQUEUE, ERRQUEUE
DB_FLT, DB_TAL = range(2)
WARNQUEUE, ERRQUEUE = range(2)
FLT_MODE_ERROR_ONLY, FLT_MODE_WARNNING_ONLY, FLT_MODE_ALL = range(3)
FLT_MODE = 2
warningQueue = []
errorQueue = []

def DB(level, msg):
   if int(level) == int(DB_FLT):
      print msg

def dumpQueueToScreen(whichQueue):
   if whichQueue == WARNQUEUE:
      print "dumping warning..."
      for warning in warningQueue:
         print warning
   elif whichQueue == ERRQUEUE:
      print "dumping warning..."
      for error in errorQueue:
         print error

def dumpQueueToFile(whichQueue, fileName):
   f = open(fileName,'w')
   if whichQueue == WARNQUEUE:
      for warning in warningQueue:
         f.write(warning)
   elif whichQueue == ERRQUEUE:
      for error in errorQueue:
         f.write(error)
   f.close()

def fltLv1(line):
   #DB(DB_TAL, line)
   symbolAry = line.split(' ')
   for symbol in symbolAry:   
      if FLT_MODE == FLT_MODE_ALL or FLT_MODE == FLT_MODE_WARNNING_ONLY:         
         if symbol == 'warning:':
            warningQueue.append(line)
      if FLT_MODE == FLT_MODE_ALL or FLT_MODE == FLT_MODE_ERROR_ONLY:
         if symbol == 'error:':
            errorQueue.append(line)

def verify():
   global DB_FLT
   if(len(sys.argv) > 1):
      FLT_MODE = int(sys.argv[1])
   if(len(sys.argv) > 2):
      DB_FLT = int(sys.argv[2])

def main():   
   print "make | python makeflt.py <MODE> <DB>"
   print "===== OUTPUT START ====="

   for line in sys.stdin:
      DB(DB_TAL, line)
      fltLv1(line)

   print "===== RESULT OUTPUT ====="

   if FLT_MODE == FLT_MODE_ALL or FLT_MODE == FLT_MODE_WARNNING_ONLY:         
      print "%d warning(s) found" %(len(warningQueue))
      #dumpQueueToScreen(WARNQUEUE)
      dumpQueueToFile(WARNQUEUE,".warningList")


   if FLT_MODE == FLT_MODE_ALL or FILE_MODE == FLT_MODE_ERROR_ONLY:
      print "%d error(s) found" %(len(errorQueue))
      #dumpQueueToScreen(ERRQUEUE)
      dumpQueueToFile(ERRQUEUE,".errorList")


   print "Have a nice day"

if __name__ == '__main__':
   verify()
   main()
