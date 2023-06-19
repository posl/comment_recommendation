def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += S - A[i] * (N - i - 1)
    print(ans)
