def solve(s):
    min = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(753-x) < min:
            min = abs(753-x)
    return min

if __name__ == '__main__':
    solve()