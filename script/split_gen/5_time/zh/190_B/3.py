def judge(n,s,d,x,y):
    for i in range(n):
        if x[i] < s and y[i] > d:
            return True
    return False
n,s,d = map(int,input().split())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
