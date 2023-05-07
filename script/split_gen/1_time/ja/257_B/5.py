def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = list(map(int,input().split()))
    for i in range(Q):
        if L[i] == 1:
            if A[0] == N:
                continue
            elif A[0] + 1 == A[1]:
                continue
            else:
                A[0] += 1
                A[1] -= 1
        elif L[i] == K:
            if A[K-1] == N:
                continue
            elif A[K-2] + 1 == A[K-1]:
                continue
            else:
                A[K-1] += 1
                A[K-2] -= 1
        else:
            if A[L[i]-1] == N:
                continue
            elif A[L[i]-2] + 1 == A[L[i]-1] or A[L[i]] + 1 == A[L[i]-1]:
                continue
            else:
                A[L[i]-1] += 1
                A[L[i]-2] -= 1
    print(*A)
