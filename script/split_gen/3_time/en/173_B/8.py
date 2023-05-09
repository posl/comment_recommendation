def main():
    n = int(input())
    verdicts = [input() for _ in range(n)]
    verdicts = [verdict for verdict in verdicts if verdict in ['AC', 'WA', 'TLE', 'RE']]
    verdicts = dict((verdict, verdicts.count(verdict)) for verdict in verdicts)
    print('AC x {}'.format(verdicts['AC']))
    print('WA x {}'.format(verdicts['WA']))
    print('TLE x {}'.format(verdicts['TLE']))
    print('RE x {}'.format(verdicts['RE']))
