def solve():
    N = int(input())
    print((998244353 - N % 998244353) % 998244353)

if __name__ == '__main__':
    solve()