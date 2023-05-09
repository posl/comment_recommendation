def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        ans += X[i]*(N-1-i) - X[i]*i
    print(ans)
