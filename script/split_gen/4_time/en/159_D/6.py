def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0]*(n+1)
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        ans += c[i]*(c[i]-1)//2
    for i in range(n):
        print(ans-c[a[i]]+1)
