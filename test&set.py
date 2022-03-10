
from glob import glob
import time
def testAndSet(newlock):
    global lock
    newlock=lock
    lock = True
    return newlock

lock=False


class a():
    
    def __init__(self,critzone):
        global lock
        self.critzone=lock
        
        
    def proces(critzone):
        while testAndSet(critzone):
            print('waiting....')
            time.sleep(3)
            
            if testAndSet(not critzone):
                print('now i am good to go')
                break
            break
        else:
            print('i am good to go')

  


proc1 = a(lock)


proc1.proces()

proc2=a(lock)

proc2.proces()

proc3=a(lock)

proc3.proces()