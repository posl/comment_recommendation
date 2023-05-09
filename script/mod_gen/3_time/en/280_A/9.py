def solve():
    h, w = map(int, input().split())
    print(sum([input().count('#') for i in range(h)]))

if __name__ == '__main__':
    solve()