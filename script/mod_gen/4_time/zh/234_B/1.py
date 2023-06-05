def max_len(x,y):
    max = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if (x[i]-x[j])**2+(y[i]-y[j])**2 > max:
                max = (x[i]-x[j])**2+(y[i]-y[j])**2
    return max**0.5
N = int(input())
x = []
y = []
for i in range(N):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
print(max_len(x,y))
