def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[0] = A[0]//2
        A.sort(reverse=True)
    print(sum(A))

if __name__ == '__main__':
    solve()