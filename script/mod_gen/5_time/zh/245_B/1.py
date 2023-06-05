def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if A[0] > 0:
        print(0)
    else:
        for i in range(1, N):
            if A[i] - A[i-1] > 1:
                print(A[i-1]+1)
                return
        print(A[N-1]+1)

if __name__ == '__main__':
    solve()