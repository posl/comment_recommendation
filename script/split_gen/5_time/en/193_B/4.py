def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min = 10**9
    for i in range(n):
        if x[i] > a[i]:
            if min > p[i]:
                min = p[i]
    if min == 10**9:
        print(-1)
    else:
        print(min)
