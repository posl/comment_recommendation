def solve():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N-sum(A))

if __name__ == '__main__':
    solve()