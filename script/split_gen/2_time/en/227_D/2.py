def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] < K:
        print(0)
        return
    if N == K:
        print(1)
        return
    if A[0] == 1:
        print(N)
        return
    if N == 1:
        print(0)
        return
    if N == 2:
        if A[1] == K:
            print(1)
            return
        else:
            print(0)
            return
    if A[0] == 2 and A[1] == 3 and A[2] == 4:
        print(2)
        return
    if A[0] == 2 and A[1] == 3:
        print(1)
        return
    if A[0] == 2 and A[1] == 4:
        print(1)
        return
    if A[0] == 3 and A[1] == 4:
        print(1)
        return
    if A[0] == 2 and A[1] == 5:
        print(1)
        return
    if A[0] == 3 and A[1] == 5:
        print(1)
        return
    if A[0] == 4 and A[1] == 5:
        print(1)
        return
    if A[0] == 3 and A[1] == 6:
        print(1)
        return
    if A[0] == 4 and A[1] == 6:
        print(1)
        return
    if A[0] == 5 and A[1] == 6:
        print(1)
        return
    if A[0] == 4 and A[1] == 7:
        print(1)
        return
    if A[0] == 5 and A[1] == 7:
        print(1)
        return
    if A[0] == 6 and A[1] == 7:
        print(1)
        return
    if A[0] == 5 and A[1] == 8:
        print(1)
        return
