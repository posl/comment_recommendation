def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        if A[i+1]-A[i]-1 != 0:
            B.append(A[i+1]-A[i]-1)
    if M == 0:
        print(1)
    elif M == N:
        print(0)
    else:
        K = min(B)
        print(sum((b-1)//K+1 for b in B))
