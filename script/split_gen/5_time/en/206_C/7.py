def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n - i - 1) - a[::-1].index(a[i])
    print(ans)
