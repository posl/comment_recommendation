def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if A[0] > B[-1]:
        print("No")
        return
    min_a = min(A)
    max_a = max(A)
    min_b = min(B)
    max_b = max(B)
    if min_a == min_b and max_a == max_b:
        print("Yes")
        return
    if K == 0:
        print("No")
        return
    for i in range(N):
        if A[i] > B[i]:
            print("No")
            return
    print("Yes")
    return
