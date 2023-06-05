def solve(h):
    if h == 1:
        return 1
    else:
        return solve(h//2)*2+1
