def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += sum(a[i:i+m]) * (i+1)
    print(ans)
