def solve():
    n, x = map(int, input().split())
    print(chr(x - 1 + ord('A')))

if __name__ == '__main__':
    solve()