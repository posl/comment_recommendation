def solve():
    N, M = [int(x) for x in input().split()]
    A = []
    for i in range(M):
        A.append([int(x) for x in input().split()][1:])
    for i in range(M):
        for j in range(i+1, M):
            if len(set(A[i]) & set(A[j])) == 0:
                print("No")
                return
    print("Yes")
