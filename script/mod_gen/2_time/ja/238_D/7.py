def solve():
    a, s = map(int, input().split())
    x = (s - a) // 2
    y = x + a
    if x >= 0 and x + y == s and x & y == a:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()