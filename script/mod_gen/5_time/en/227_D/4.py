def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(N - sum(A[:K]))

if __name__ == '__main__':
    solve()