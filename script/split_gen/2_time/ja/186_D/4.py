def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += i * A[i] - (N - i - 1) * A[i]
    print(ans)
