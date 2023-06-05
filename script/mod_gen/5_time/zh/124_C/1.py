def solve(s):
    return min(s.count('0'), s.count('1')) * 2

if __name__ == '__main__':
    solve()