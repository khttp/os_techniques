import time
lock=False
tasks=['task 1','task 2','task 3']
def test_and_set(newlock):
    global lock
    newlock = lock
    lock=True
    return newlock
def reset_lock(newlock):
    global lock
    lock=False
while tasks:
    while not test_and_set(lock):
        ## execution
        for task in tasks:
            print(f'{task} is good to go')
            time.sleep(2)
            print(f'{task} is excuted')
            print('=========')
            time.sleep(0.4)
            tasks.remove(task)

        ##reset the lock after finishing the task
            reset_lock(lock)
            break
    