def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N - 10**(i-1) + 1) * i
        ans %= 998244353
    print(ans)
