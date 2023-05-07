def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(N-2):
        A[i+1] = min(B[i], B[i+1])
    print(sum(A))
    return 0

if __name__ == '__main__':
    solve()