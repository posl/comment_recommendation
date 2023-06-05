def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(N):
        D[C[i]] += 1
    ans = 0
    for i in range(N):
        ans += D[B[A[i] - 1]]
    print(ans)
