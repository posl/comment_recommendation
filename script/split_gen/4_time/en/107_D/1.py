def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i + 1)
    B.sort()
    if N % 2 == 1:
        median = B[N // 2]
    else:
        median = (B[N // 2] + B[N // 2 - 1]) // 2
    ans = 0
    for i in range(N):
        ans += abs(B[i] - median)
    print(ans)
