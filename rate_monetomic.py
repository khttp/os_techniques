class process():
    def __init__ (self,priority,exec_time):
        self.priority=priority
        self.exec_time=exec_time
    
    def excuting(self):
        print(f'task with priority {self.priority} is now excuting it takes {self.exec_time}')

pro1=process(5, 3)
pro2=process(9, 2)
pro3=process(10, 3)

processes=[pro1,pro3,pro2]
priorities=[pro1.priority,pro2.priority,pro3.priority]
while processes:
    for pro in processes:
        if pro.priority == min(priorities):
            pro.excuting()
            processes.remove(pro)
            priorities.remove(pro.priority)
            break
    