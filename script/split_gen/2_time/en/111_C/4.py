def main():
    n = int(input())
    v = list(map(int,input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    v1.sort()
    v2.sort()
    v1c = []
    v2c = []
    v1c.append([v1[0],1])
    v2c.append([v2[0],1])
    for i in range(1,n//2):
        if v1[i] == v1c[len(v1c)-1][0]:
            v1c[len(v1c)-1][1] += 1
        else:
            v1c.append([v1[i],1])
        if v2[i] == v2c[len(v2c)-1][0]:
            v2c[len(v2c)-1][1] += 1
        else:
            v2c.append([v2[i],1])
    #print(v1c)
    #print(v2c)
    if v1c[-1][0] == v2c[-1][0]:
        if len(v1c) == 1:
            print(v2c[-1][1])
        elif len(v2c) == 1:
            print(v1c[-1][1])
        else:
            print(min(n-v1c[-1][1]-v2c[-2][1],n-v1c[-2][1]-v2c[-1][1]))
    else:
        print(n-v1c[-1][1]-v2c[-1][1])
main()
I don't know why it's not working. Can anyone please help me to find the error?
I can't see anything wrong with your code, but I can't reproduce the error. Can you post the full error message?
I can't see anything wrong with your code, but I can't reproduce the error. Can you post the full error message?
It's not showing any error. It's just showing WA.
I think it's because of the sample input 2. I'm not sure why it's not working.
It's not showing any error. It's just showing WA.
I think it's because of the sample input 2. I'm not sure why it's not working.
I can't reproduce the error, so I can't help you.
I can't reproduce the error
