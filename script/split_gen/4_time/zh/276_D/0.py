def f(x):
    if x%2==0:
        return x/2
    elif x%3==0:
        return x/3
    else:
        return -1
n = int(input())
a = list(map(int,input().split()))
ans = 0
while True:
    flag = True
    for i in range(n):
        if f(a[i])!=-1:
            a[i] = f(a[i])
            flag = False
    if flag:
        break
    ans += 1
for i in range(n):
    if a[i]!=a[0]:
        ans = -1
        break
print(ans)
