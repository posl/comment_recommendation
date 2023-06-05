def solve():
    n, a, b = map(int, input().split())
    s = input()
    if a < b:
        print(a*n+b)
    else:
        print(b*n)

if __name__ == '__main__':
    solve()