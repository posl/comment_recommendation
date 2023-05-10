def solve(s, t):
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False

if __name__ == '__main__':
    solve()