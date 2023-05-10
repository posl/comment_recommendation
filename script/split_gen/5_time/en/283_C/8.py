def solve(s):
    #print(f"solve({s})")
    if s == 0:
        return 0
    elif s % 10 == 0:
        return 1 + solve(s // 10)
    elif s % 100 == 0:
        return 1 + solve(s // 100)
    else:
        return 1 + min(solve(s - 1), solve(s - (s % 10)))
