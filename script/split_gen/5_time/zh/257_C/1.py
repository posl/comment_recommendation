def f(x):
    #print(x)
    ans = 0
    for i in range(n):
        if s[i] == '1' and w[i] >= x:
            ans += 1
        elif s[i] == '0' and w[i] < x:
            ans += 1
    return ans
n = int(input())
s = input()
w = list(map(int, input().split()))
l = 0
r = 10**9 + 1
while r-l > 1:
    mid = (l+r)//2
    if f(mid) == n:
        break
    elif f(mid) < n:
        r = mid
    else:
        l = mid
print(mid)
