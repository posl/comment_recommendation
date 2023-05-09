def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        if A[0] != A[1]:
            print(0)
            return
        if A[-1] != A[-2]:
            print(0)
            return
        for i in range(2, N * 2, 2):
            if A[i] != A[i + 1]:
                print(0)
                return
    else:
        if A[0] != A[1]:
            print(0)
            return
        if A[-1] != A[-2]:
            print(0)
            return
        for i in range(2, N * 2 - 1, 2):
            if A[i] != A[i + 1]:
                print(0)
                return
        if A[N * 2 - 1] != A[N * 2 - 2]:
            print(0)
            return
    print(pow(2, N // 2, 10 ** 9 + 7))

if __name__ == '__main__':
    solve()