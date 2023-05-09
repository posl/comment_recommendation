def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    D = [0 for i in range(N+1)]
    for i in range(N):
        D[A[i]-1] += 1
        D[A[i]+B[i]-1] -= 1
    for i in range(1,N+1):
        D[i] += D[i-1]
    D.pop()
    D.sort()
    print(*D)
