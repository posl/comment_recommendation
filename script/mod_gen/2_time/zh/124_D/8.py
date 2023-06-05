def solve(s):
    a = s.count("0")
    b = s.count("1")
    return min(a,b)*2

if __name__ == '__main__':
    solve()