def problem173_b():
    N = int(input())
    verdicts = []
    for i in range(N):
        verdicts.append(input())
    print('AC x', verdicts.count('AC'))
    print('WA x', verdicts.count('WA'))
    print('TLE x', verdicts.count('TLE'))
    print('RE x', verdicts.count('RE'))
