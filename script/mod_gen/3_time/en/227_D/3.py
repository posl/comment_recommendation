def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == K:
        print(1)
        return
    if K == 1:
        print(N)
        return
    if A[-1] == 1:
        print(N)
        return
    if A[0] == A[-1]:
        print(1)
        return
    if A[0] == 1:
        print(N - A.count(1))
        return
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if A[0] == A[1]:
        print(1)
        return
    if A[1] == A[2]:
        print(2)
        return
    if A[-1] == A[-2]:
        print(N - 1)
        return
    if A[-2] == A[-3]:
        print(N - 2)
        return
    if N == 4:
        print(2)
        return
    if A[0] == A[1] and A[1] == A[2]:
        print(1)
        return
    if A[1] == A[2] and A[2] == A[3]:
        print(2)
        return
    if A[-1] == A[-2] and A[-2] == A[-3]:
        print(N - 1)
        return
    if A[-2] == A[-3] and A[-3] == A[-4]:
        print(N - 2)
        return
    if N == 5:
        print(2)
        return
    if A[0] == A[1] and A[1] == A[2] and A[2] == A[3]:
        print(1)
        return
    if A[1] == A[2] and A[2] == A[3] and A[3] == A[4]:
        print(2)
        return
    if A[-1] == A[-2] and A[-2] == A[-3] and A[-3] == A[-4]:
        print(N - 1)
        return
    if A[-2]

if __name__ == '__main__':
    main()