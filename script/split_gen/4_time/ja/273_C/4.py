def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    K = [0] * N
    for i in range(N):
        K[i] = A.count(A[i])
    ans = [0] * N
    for i in range(N):
        ans[i] = N - sum(K[:i])
    for i in ans:
        print(i)
