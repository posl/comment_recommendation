def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (A[-1] + 1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(N):
        for j in range(A[i], A[-1] + 1, A[i]):
            ans += B[j]
        B[A[i]] -= 1
    print(ans)
