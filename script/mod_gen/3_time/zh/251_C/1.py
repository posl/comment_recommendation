def problems251_c():
    n=int(input())
    s=[]
    t=[]
    for i in range(n):
        temp=input().split()
        s.append(temp[0])
        t.append(int(temp[1]))
    max=0
    for i in range(n):
        if t[i]>max:
            max=t[i]
    for i in range(n):
        if t[i]==max:
            maxs=s[i]
            break
    for i in range(n):
        if s[i]==maxs and t[i]==max:
            print(i+1)
            break

if __name__ == '__main__':
    problems251_c()