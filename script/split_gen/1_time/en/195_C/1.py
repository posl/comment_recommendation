def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * 3 * (10 ** (i - 1))
    ans += (N - 10 ** (len(str(N)) - 1) + 1) * len(str(N))
    print(ans)
