def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    S = [0] * N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = S[i - 1] + A[i]
    ans = 0
    for i in range(1, N):
        ans += i * A[i] - S[i - 1]
    print(ans * 2)
