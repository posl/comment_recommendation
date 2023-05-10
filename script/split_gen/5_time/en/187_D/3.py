def solve():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = [a[i]+b[i] for i in range(n)]
    c.sort(reverse=True)
    print(sum(c[::2])-sum(c[1::2]))
