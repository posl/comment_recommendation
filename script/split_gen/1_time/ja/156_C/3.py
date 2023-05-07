def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(1, n):
        ans += (x[i] - x[i - 1]) * i * (n - i)
    print(ans)
