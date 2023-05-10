def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[-K:]))
    return 0

if __name__ == '__main__':
    solve()