def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        if a[i] == a[i+1]:
            ans += 1
        if b[i] == b[i+1]:
            ans += 1
    print(ans)
