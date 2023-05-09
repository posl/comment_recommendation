def div3(x):
    if x%3 == 0:
        return div3(x/3) + 1
    else:
        return 0
N = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(N):
    count += div3(a[i])
print(count)
