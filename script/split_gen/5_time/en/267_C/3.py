def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*(n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    c = [0]*(n+1)
    for i in range(n):
        if i >= m:
            c[i+1] = max(c[i], b[i+1]-b[i+1-m])
        else:
            c[i+1] = max(c[i], b[i+1])
    ans = 0
    for i in range(n+1):
        if i >= m:
            ans = max(ans, c[i]+b[i]-b[i-m])
        else:
            ans = max(ans, c[i]+b[i])
    print(ans)
