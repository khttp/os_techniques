files=[11,45,78,0,34,66]
head=45

estimate_time = 0

for file in files:
    estimate_time+=abs(file-head)
    head=file
print(estimate_time)    