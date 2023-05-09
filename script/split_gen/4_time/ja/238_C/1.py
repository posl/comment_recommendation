def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += len(str(i))
    print(ans % 998244353)
