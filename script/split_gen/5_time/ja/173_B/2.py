def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ac = s.count('AC')
    wa = s.count('WA')
    tle = s.count('TLE')
    re = s.count('RE')
    print('AC x', ac)
    print('WA x', wa)
    print('TLE x', tle)
    print('RE x', re)
