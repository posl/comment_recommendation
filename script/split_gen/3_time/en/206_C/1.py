def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += (n - 1 - i) * (a[i+1] - a[i])
    print(ans)
