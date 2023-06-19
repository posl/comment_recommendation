def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    ans = 0
    for i in range(N - 1):
        if B[i] > B[i + 1]:
            ans += 1
    print(ans + 1)
