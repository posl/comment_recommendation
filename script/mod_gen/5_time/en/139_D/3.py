def solve():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(sum(range(1, n)))
solve()

if __name__ == '__main__':
    solve()