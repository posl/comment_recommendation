def f(k):
    arc = 0
    abc = 0
    for i in range(n):
        if a[i] >= k:
            arc += 1
        else:
            abc += 1
    if arc == abc:
        return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
l = 0
r = max(a)+1
while r - l > 1:
    m = (l + r) // 2
    if f(m):
        l = m
    else:
        r = m
print(l)

if __name__ == '__main__':
    f()