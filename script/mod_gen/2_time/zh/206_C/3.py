def solve(n):
    sum = 0
    day = 1
    while sum < n:
        sum += day
        day += 1
    return day - 1

if __name__ == '__main__':
    solve()