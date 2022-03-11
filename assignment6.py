# Take a File Sample.txt & find where is the duplicate line

i=0
sample_list = []
fr = open("sample1.txt", "r")

for each in fr:
    if each in sample_list:
        print("duplicate line is:",each)
        print(i)
    sample_list.append(each)
    i=i+1
print(sample_list)

    
    
