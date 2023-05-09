def solve():
    N, K = map(int, input().split())
    if K % 2 == 0:
        a = N // K
        b = N // (K // 2) - a
        print(a**3 + b**3)
    else:
        a = N // K
        print(a**3)

if __name__ == '__main__':
    solve()