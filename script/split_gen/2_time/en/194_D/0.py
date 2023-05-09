def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n / i) * (1 / n)
    print(ans)
