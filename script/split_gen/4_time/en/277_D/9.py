def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] + ans) % m
    print(ans)
