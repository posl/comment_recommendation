def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ans = [0] * N
    for i in range(K):
        ans[A[i]-1] = 1
    for i in range(Q):
        for j in range(K):
            if ans[A[L[j]-1]-1] == 1 and A[L[j]-1] != N:
                ans[A[L[j]-1]-1] = 0
                ans[A[L[j]-1]] = 1
                A[L[j]-1] += 1
    for i in range(N):
        if ans[i] == 1:
            print(i+1, end=" ")
    print()
