def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += a[i]*(n-i-1)
    print(ans + a[-1])
