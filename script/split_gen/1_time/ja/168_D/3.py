def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [1 for i in range(N)]
    for i in range(M):
        if ans[A[i]-1] != A[i]:
            ans[B[i]-1] = A[i]
        else:
            ans[B[i]-1] = B[i]
    print("Yes")
    for i in range(1, N):
        print(ans[i])
