def solve():
    h, w = map(int, input().split())
    print(sum([input().count('#') for i in range(h)]))
