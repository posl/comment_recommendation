def solve():
    s = raw_input()
    t = raw_input()
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s == t:
            return True
        s = s[-1] + s[:-1]
    return False

if __name__ == '__main__':
    solve()