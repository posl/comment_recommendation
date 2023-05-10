def main():
    n,d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        x,y = map(int, input().split())
        l.append(x)
        r.append(y)
    l.sort()
    r.sort()
    ans = 0
    for i in range(n):
        ans += 1
        if i != n-1:
            if l[i+1] - r[i] < d:
                ans -= 1
    print(ans)
