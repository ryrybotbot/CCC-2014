names = {}
out = "good"

students = int(input())
data1 = input().split()
data2 = input().split()
data3 = [0]*students
for k in range(students):
    if (data1[k]==data2[k]):
        out="bad"
        break
    else:
        data3[data1.index(data2[k])]+=1
if (not out == "bad"):
    for k in range(students):
        if (not data3[k]==1):
            out = "bad"
if (not out == "bad"):
    for k in range(students):
        if (not data2[data1.index(data2[k])]==data1[k]):
            out = "bad"
            break
print(out)
