def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    K = K % N
    for i in range(K):
        A = list(map(lambda x: A[x - 1], A))
    print(A[0])

if __name__ == '__main__':
    solve()