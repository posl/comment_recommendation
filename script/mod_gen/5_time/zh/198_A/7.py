def solve():
    N = int(input())
    if N % 2 == 1:
        print(0)
    else:
        print(2 ** (N // 2))

if __name__ == '__main__':
    solve()