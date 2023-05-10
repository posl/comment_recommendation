def solve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for i in range(M)]
    A.sort(key=lambda x: len(x))
    if len(A[0]) == 1:
        print("No")
        return
    for i in range(1, M):
        if len(A[i]) == 1:
            print("No")
            return
        if len(A[i]) == 2:
            if A[i][0] != A[i - 1][0] or A[i][1] != A[i - 1][1]:
                print("No")
                return
        else:
            if A[i][0] != A[i - 1][0] or A[i][1] != A[i - 1][2]:
                print("No")
                return
            A[i][1] = A[i - 1][1]
            A[i][2] = A[i - 1][2]
    print("Yes")
