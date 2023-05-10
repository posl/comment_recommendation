def cal_average(a,b):
    return (a+b)/2
n = int(input())
v = list(map(int,input().split()))
for i in range(n-1):
    v.sort()
    v[0] = cal_average(v[0],v[1])
    v.pop(1)
print(v[0])
