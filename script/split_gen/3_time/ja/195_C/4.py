def main():
    N = int(input())
    ans = 0
    for i in range(1,15):
        ans += (N - 10**i + 1) * i
        N = 10**i - 1
    print(ans)
