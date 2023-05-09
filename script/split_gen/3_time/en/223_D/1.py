def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, M)
    #print(A)
    #print(B)
    ans = []
    ans.append(1)
    for i in range(2, N+1):
        ans.append(i)
    #print(ans)
    for i in range(M):
        for j in range(N-1):
            if A[i] == ans[j] and B[i] == ans[j+1]:
                tmp = ans[j+1]
                ans[j+1] = ans[j]
                ans[j] = tmp
    #print(ans)
    for i in range(M):
        for j in range(N-1):
            if A[i] == ans[j] and B[i] == ans[j+1]:
                print("-1")
                return
    print(*ans)
