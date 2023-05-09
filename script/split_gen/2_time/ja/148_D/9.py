def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        if B[i] > i + 1:
            ans += B[i] - (i + 1)
    print(ans)
