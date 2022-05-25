class process():
    def __init__ (self,dead_line,exec_time):
        self.dead_line=dead_line
        self.exec_time=exec_time
    
    def excuting(self):
        print(f'task with deadline {self.dead_line} is now excuting it takes {self.exec_time}')

pro1=process(5, 3)
pro2=process(9, 2)
pro3=process(10, 3)

processes=[pro1,pro3,pro2]
deadline=[pro1.dead_line,pro2.dead_line,pro3.dead_line]
while processes:
    for pro in processes:
        if pro.dead_line == min(deadline):
            pro.excuting()
            processes.remove(pro)
            deadline.remove(pro.dead_line)
            break
    