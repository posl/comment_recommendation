def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*(m+1)
    for i in a:
        b[i] += 1
    ans = 0
    for i in range(m):
        ans += b[i]*i
    ans += b[m]*m
    print(ans)
