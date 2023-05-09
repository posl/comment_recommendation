def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x:x[1],reverse=True)
    i = 0
    for j in range(M):
        for k in range(BC[j][0]):
            if A[i] < BC[j][1]:
                A[i] = BC[j][1]
                i += 1
            else:
                break
    print(sum(A))
