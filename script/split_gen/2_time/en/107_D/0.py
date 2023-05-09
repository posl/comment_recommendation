def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (i + 1) * (N - i) * A[i]
    ans = ans // N
    print(ans)
