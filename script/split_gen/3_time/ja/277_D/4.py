def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = [0]*N
    for i in range(N):
        B[i] = A[i] % M
    C = [0]*M
    for i in range(N):
        C[B[i]] += 1
    C.sort()
    ans = 0
    for i in range(M):
        if C[i] == 0:
            continue
        else:
            ans += C[i]*i
            C[i+1] += C[i]
    print(ans)
