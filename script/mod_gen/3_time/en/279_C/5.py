def solve():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    print("Yes" if sorted(s) == sorted(t) else "No")

if __name__ == '__main__':
    solve()