def solve(n,q,a,x):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - x
    b.sort()
    s = sum(b)
    res = 0
    for i in range(n):
        if b[i] > 0:
            break
        res += -b[i]
    for i in range(n-1,-1,-1):
        if b[i] < 0:
            break
        res += b[i]
    return res
n,q = map(int,input().split())
a = list(map(int,input().split()))
x = [0] * q
for i in range(q):
    x[i] = int(input())
for i in range(q):
    print(solve(n,q,a,x[i]))

if __name__ == '__main__':
    solve()