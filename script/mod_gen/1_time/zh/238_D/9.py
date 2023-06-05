def solve(a, s):
    if a > s:
        return "No"
    elif a == s:
        return "Yes"
    else:
        if s % 2 == 1:
            return "No"
        else:
            if a % 2 == 1:
                return "Yes"
            else:
                return solve(a >> 1, s >> 1)

if __name__ == '__main__':
    solve()