def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    B = []
    for i in range(M+1):
        B.append(A[i+1]-A[i]-1)
    B.sort()
    B.reverse()
    ans = 0
    for i in range(M+1):
        ans += B[i]*(i+1)
    print(ans)
