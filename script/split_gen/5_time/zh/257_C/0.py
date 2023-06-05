def f(x):
    cnt = 0
    for i in range(n):
        if s[i] == "0" and w[i] < x:
            cnt += 1
        elif s[i] == "1" and w[i] >= x:
            cnt += 1
    return cnt
n = int(input())
s = input()
w = list(map(int, input().split()))
l = 0
r = 1000000001
while r - l > 1:
    mid = (l + r) // 2
    if f(mid) == n:
        l = mid
    else:
        r = mid
print(l)
