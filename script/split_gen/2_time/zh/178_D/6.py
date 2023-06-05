def solve():
    N = int(input())
    if N == 1:
        print(0)
        return
    print((10**N - 2*9**N + 8**N) % (10**9 + 7))
solve()
