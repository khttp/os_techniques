s=1
tasks=['task1','task2','task3','task4']
def p(s):
    
    while (s<=0):
        pass
    s-=1
    return s
def v(s):
    s+=1
    return s
    
while tasks:
    for task in tasks:
        if s>0 :
            s=p(s)
            print(f'{task} is now executing')
            tasks.remove(tasks[0])
        else:
            s=v(s)