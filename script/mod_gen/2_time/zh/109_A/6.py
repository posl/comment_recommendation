def solve(n):
    print(n * 2 - 1, n * 2 - 2)
    for i in range(1, n):
        print(i, i + 1, 0)
        print(i, i + 1, 10 ** 5 - i)

if __name__ == '__main__':
    solve()