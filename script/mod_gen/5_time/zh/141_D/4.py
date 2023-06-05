def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(M):
        A[-1] //= 2
        A.sort()
    print(sum(A))

if __name__ == '__main__':
    solve()