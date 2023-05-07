def solve():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(N):
        K, *B = map(int, input().split())
        for b in B:
            A[b-1] += 1
    print(A.count(N))

if __name__ == '__main__':
    solve()