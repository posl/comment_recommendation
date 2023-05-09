def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            count += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            count += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            count += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(count)

if __name__ == '__main__':
    solve()