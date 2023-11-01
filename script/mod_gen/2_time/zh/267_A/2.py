def solve(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return 7 - days.index(day)

if __name__ == '__main__':
    solve()