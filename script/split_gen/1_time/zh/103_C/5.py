def f(x):
    #print(x)
    global N
    global a
    result = 0
    for i in range(0, N):
        result += x % a[i]
    return result
N = int(input())
a = list(map(int, input().split()))
l = 0
r = 10**18
while r - l > 1:
    mid = (r + l) // 2
    #print("l = %d, r = %d, mid = %d" % (l, r, mid))
    if f(mid) <= f(mid + 1):
        r = mid
    else:
        l = mid
print(f(r))
