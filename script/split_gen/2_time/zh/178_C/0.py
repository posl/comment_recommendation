def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        mod = 10 ** 9 + 7
        ans = 10 ** n - 2 * 9 ** n + 8 ** n
        print(ans % mod)
