def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for _ in range(m):
        i, j = map(int, input().split())
        x.append(i)
        y.append(j)
    
    now = t
    for i in range(n-1):
        now -= a[i]
        if now <= 0:
            print("No")
            return
        if i+1 in x:
            now += y[x.index(i+1)]
            if now > t:
                now = t
    
    print("Yes")
