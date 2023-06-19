def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ans = [0] * N
    for i in range(K):
        ans[A[i] - 1] += 1
    for i in range(Q):
        ans = ans[-1:] + ans[:-1]
        ans[L[i] - 1] += 1
    for i in range(N):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")
