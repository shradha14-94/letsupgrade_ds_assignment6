#give 1-10 number non repeated


import random
list1 = list(range(1,11))
print(list1)
random.shuffle(list1)
for each in list1:
    input("press enter to find the next value")
    print(each)