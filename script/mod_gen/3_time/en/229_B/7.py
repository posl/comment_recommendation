def solve(a, b):
    if a + b >= 10 ** 18:
        return "Hard"
    else:
        return "Easy"

if __name__ == '__main__':
    solve()