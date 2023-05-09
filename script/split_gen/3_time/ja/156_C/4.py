def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        ans += (i * x[i] - (n - i - 1) * x[i])
    print(ans)
