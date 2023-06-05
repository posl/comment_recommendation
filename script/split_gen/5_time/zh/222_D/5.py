def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= 998244353
    print(ans)
