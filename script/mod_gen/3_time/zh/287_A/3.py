def solve():
    n = int(input())
    s = [input() for i in range(n)]
    print("Yes" if s.count("For") > n // 2 else "No")
solve()
