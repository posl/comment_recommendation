def solve():
    s = input()
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - days.index(s))

if __name__ == '__main__':
    solve()