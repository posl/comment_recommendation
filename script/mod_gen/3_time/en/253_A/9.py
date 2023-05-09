def solve(a, b, c):
    if a < b < c or c < b < a:
        return "Yes"
    return "No"

if __name__ == '__main__':
    solve()