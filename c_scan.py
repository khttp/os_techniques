files=[0,11,78,34,66,99]
head=45

estimate_time = 0
bigger_vals=[i for i in files if i >head]
bigger_vals.sort()
#print(bigger_vals)

smaller_vals=[i for i in files if i <head]
smaller_vals.sort()

print(smaller_vals)


for i in bigger_vals:

    estimate_time+=abs(head-i)
    head=i

for i in smaller_vals:
    estimate_time+=abs(head-i)
    head=i
print(estimate_time)