def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0 and A[-1] == 0:
        print(0)
        exit()
    if A[0] == 0 or A[-1] == 0:
        print(-1)
        exit()
    if N == 2:
        if (A[0] + A[1]) % 2 == 0:
            print(A[0] + A[1])
            exit()
        else:
            print(-1)
            exit()
    if N == 3:
        if (A[0] + A[1]) % 2 == 0:
            print(A[0] + A[1])
            exit()
        if (A[0] + A[2]) % 2 == 0:
            print(A[0] + A[2])
            exit()
        if (A[1] + A[2]) % 2 == 0:
            print(A[1] + A[2])
            exit()
        if (A[0] + A[1] + A[2]) % 2 == 0:
            print(A[0] + A[1] + A[2])
            exit()
        else:
            print(-1)
            exit()
    if N >= 4:
        if (A[0] + A[-1]) % 2 == 0:
            print(A[0] + A[-1])
            exit()
        if (A[0] + A[-2]) % 2 == 0:
            print(A[0] + A[-2])
            exit()
        if (A[1] + A[-1]) % 2 == 0:
            print(A[1] + A[-1])
            exit()
        if (A[1] + A[-2]) % 2 == 0:
            print(A[1] + A[-2])
            exit()
        if (A[0] + A[-3]) % 2 == 0:
            print(A[0] + A[-3])
            exit()
        if (A[1] + A[-3]) % 2 == 0:
            print(A[1] + A[-3])
            exit()
        if (A[2] + A

if __name__ == '__main__':
    main()