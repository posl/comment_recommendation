def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    D = [0]*(N+1)
    for i in range(N):
        D[0] += A[i]-1
        D[0] -= max(0,A[i]+B[i]-10**100-1)
        D[1] += min(B[i],10**100-A[i]+1)
        D[min(B[i],N)] -= min(B[i],10**100-A[i]+1)
    for i in range(1,N+1):
        D[i] += D[i-1]
    print(*D[:N])
