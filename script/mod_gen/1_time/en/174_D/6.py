def solve():
    N = int(input())
    S = input()
    R = S.count("R")
    W = N - R
    ans = min(R, W)
    print(ans)

if __name__ == '__main__':
    solve()