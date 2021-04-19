#TLP: AMBER (closed communities to trusted individuals only) 
#Name: Babuk Ransomware Vaccine 
#Author: CERT Sogeti ESEC Threat Intelligence Team 
#Description: This vaccine prevents the Babuk Ransomware execution through Mutex creation 
#Contact: sogetiesecctiteam.eur@capgemini.com 
 
import win32event 
import win32file 
import win32con 
from threading import Thread 
import time 
import os 
from subprocess import Popen, PIPE 
 
# Thread keeping the mutexes open
class MutexThread (Thread): 
   def __init__(self, mutexname): 
      Thread.__init__(self) 
      self.mutexname = mutexname 
 
   def run(self): 
      mutex = win32event.CreateMutex(None, True, self.mutexname) 
      while (True): 
          time.sleep(1) 
 
# Arrays containing the threads & mutexes
mutexNames = [] 
threads = [] 
 
# We added the last strain’s mutex 
mutexNames.append("DoYouWantToHaveSexWithCoungDong") 
threads.append(MutexThread(mutexNames[0])) 
threads[0].start() 
 
for i in range(1, 11): 
    mutexNames.append("babuk_v" + str(i)) 
    threads.append(MutexThread(mutexNames[i])) 
    threads[i].start() 
 
# Then we create the file in AppData/Roaming 
# We also forbid other access with the shareMode, just in case 
fileName = os.getenv("APPDATA") + "\ecdh_pub_k.bin" 
# Impossible to access the file until the handle is closed 
shareMode = 0    
securityAttributes = 0                             
creationDisposition = win32con.CREATE_NEW          
fileAttributes = win32con.FILE_ATTRIBUTE_NORMAL 
templateFile = 0 
 
desiredAccess = win32con.GENERIC_READ 
  
file = win32file.CreateFile( 
   fileName, 
   desiredAccess, 
   shareMode, 
   None, 
   creationDisposition, 
   fileAttributes, 
   None, 
) 
 
While(1): 
  time.sleep(1) 
 
file.Close()
