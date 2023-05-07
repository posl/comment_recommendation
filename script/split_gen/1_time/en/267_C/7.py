def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    B = []
    for i in range(M):
        B.append(A[i])
    B.sort(reverse=True)
    #print(B)
    ans = 0
    for i in range(M):
        ans += (i+1) * B[i]
    print(ans)
