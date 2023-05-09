def solve():
    N = int(input())
    if N % 2 == 0:
        print(int(N/2))
    else:
        print(int(N/2) + 1)

if __name__ == '__main__':
    solve()