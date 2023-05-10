def solve():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    return sum(p) - p[0]//2
print(solve())

if __name__ == '__main__':
    solve()