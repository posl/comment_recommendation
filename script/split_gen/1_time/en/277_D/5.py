def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == 1:
        print(0)
        return
    if A[0] != 0:
        print(sum(A))
        return
    if A[-1] == M-1:
        print(0)
        return
    if A[-1] == M-2:
        print(A[-1])
        return
    if A[-1] == M-3:
        print(A[-1] + A[-2])
        return
    if A[-2] == M-1:
        print(A[-1])
        return
    if A[-2] == M-2:
        print(A[-1] + A[-2])
        return
    if A[-2] == M-3:
        print(A[-1] + A[-2])
        return
    if A[-3] == M-1:
        print(A[-1] + A[-2])
        return
    if A[-3] == M-2:
        print(A[-1] + A[-2])
        return
    if A[-3] == M-3:
        print(A[-1] + A[-2])
        return
    if A[-4] == M-1:
        print(A[-1] + A[-2])
        return
    if A[-4] == M-2:
        print(A[-1] + A[-2])
        return
    if A[-4] == M-3:
        print(A[-1] + A[-2])
        return
    print(A[-1] + A[-2])
