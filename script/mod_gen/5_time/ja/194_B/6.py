def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(min(max(a), max(b)))
    return 0

if __name__ == '__main__':
    solve()