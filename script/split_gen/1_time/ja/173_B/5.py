def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(n):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
        elif s[i] == 'TLE':
            tle += 1
        elif s[i] == 'RE':
            re += 1
    print('AC x', ac)
    print('WA x', wa)
    print('TLE x', tle)
    print('RE x', re)
main()
