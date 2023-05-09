def main():
    N = int(input())
    verdicts = [input() for _ in range(N)]
    AC = 0
    WA = 0
    TLE = 0
    RE = 0
    for verdict in verdicts:
        if verdict == 'AC':
            AC += 1
        elif verdict == 'WA':
            WA += 1
        elif verdict == 'TLE':
            TLE += 1
        else:
            RE += 1
    print('AC x {}'.format(AC))
    print('WA x {}'.format(WA))
    print('TLE x {}'.format(TLE))
    print('RE x {}'.format(RE))

if __name__ == '__main__':
    main()