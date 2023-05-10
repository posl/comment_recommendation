def main():
    n, a, b = map(int, input().split(" "))
    ans = pow(2, n, 10**9 + 7) - 1
    for i in range(n - a, n - b):
        ans -= pow(2, i, 10**9 + 7)
    print(ans % (10**9 + 7))
