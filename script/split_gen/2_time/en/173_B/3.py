def main():
    N = int(input())
    verdicts = [input() for _ in range(N)]
    AC = verdicts.count('AC')
    WA = verdicts.count('WA')
    TLE = verdicts.count('TLE')
    RE = verdicts.count('RE')
    print('AC x', AC)
    print('WA x', WA)
    print('TLE x', TLE)
    print('RE x', RE)
