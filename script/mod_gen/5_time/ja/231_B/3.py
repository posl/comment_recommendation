def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(s, key=s.count))

if __name__ == '__main__':
    solve()