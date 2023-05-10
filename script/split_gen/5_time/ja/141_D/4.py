def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A.append(0)
    i = 0
    while i < N and M > 0:
        if A[i] > A[i+1]:
            A[i] //= 2
            M -= 1
        else:
            i += 1
    print(sum(A))
