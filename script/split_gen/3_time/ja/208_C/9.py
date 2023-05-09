def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    #print(A)
    B = []
    for i in range(1, N+1):
        B.append(A[i] - A[i-1] - 1)
    #print(B)
    ans = []
    for i in range(N):
        ans.append((K - 1) // N + 1)
    #print(ans)
    for i in range(N):
        if (K - 1) // N + 1 > B[i]:
            K -= B[i]
            ans[i] += B[i]
        else:
            ans[i] += (K - 1) % N
            break
    for i in range(N):
        print(ans[i])
