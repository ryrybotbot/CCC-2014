tests = int(input())
outputs = ["Y"]*tests
for asd in range(tests):
    N = int(input())
    curr = 0
    queue=[0]*N
    hold=[]
    complete = "Y"
    for k in range(N):
        queue[N-k-1]=int(input())
    while (not curr == N):
        if (len(queue) > 0 and (queue[0]==(curr+1))):
            queue.pop(0)
            curr+=1
        elif(len(hold) >0 and (hold[0]==(curr+1))):
            hold.pop(0)
            curr+=1
        elif(len(queue)>0):
            hold= [queue.pop(0)]+hold
        else:
            complete = "N"
            break
    outputs[asd]=complete
for k in range(len(outputs)):
    print(outputs[k])
