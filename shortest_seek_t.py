files=[11,78,0,34,66]
head=45

estimate_time = 0

for i in range(len(files)):
    estimate_time+=abs(head-min(files))
    head=min(files)
    files.remove(min(files))
print(estimate_time)    