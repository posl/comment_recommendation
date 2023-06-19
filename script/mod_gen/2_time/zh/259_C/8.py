def solve(s,t):
    if len(s) > len(t):
        return False
    elif len(s) == len(t):
        return s == t
    else:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

if __name__ == '__main__':
    solve()