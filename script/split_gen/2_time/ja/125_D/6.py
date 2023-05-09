def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = A[:]
    for i in range(N - 1):
        B[i + 1] = A[i] + A[i + 1]
    ans = 0
    for i in range(N):
        ans += B[i]
    print(ans)
