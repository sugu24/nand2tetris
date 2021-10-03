import sys

file_a = []
file_b = []
file_name = "Bat"
with open(sys.argv[1]+"/" + file_name + ".vm", mode="r") as f:
    for s in f:
        file_a.append(s)
with open(sys.argv[1]+"/" + file_name + "-.vm", mode="r") as f:
    for s in f:
        file_b.append(s)
i = 1
for A,B in zip(file_a,file_b):
    for a, b in zip(A,B):
        if a!=b:print(i,"   ",a,b)
        #else:print("-----",a,b)
    i += 1