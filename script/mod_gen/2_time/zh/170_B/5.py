def solve():
    x, y = map(int, input().split())
    for i in range(x + 1):
        if i * 4 + (x - i) * 2 == y:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    solve()