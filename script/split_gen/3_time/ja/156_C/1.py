def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += X[i] * i - X[i] * (N - i - 1)
    print(ans)
