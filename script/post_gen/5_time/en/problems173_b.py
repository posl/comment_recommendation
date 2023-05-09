Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
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
    print('AC x ' + str(ac))
    print('WA x ' + str(wa))
    print('TLE x ' + str(tle))
    print('RE x ' + str(re))

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print("AC x " + str(s.count("AC")))
    print("WA x " + str(s.count("WA")))
    print("TLE x " + str(s.count("TLE")))
    print("RE x " + str(s.count("RE")))

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("AC x " + str(s.count("AC")))
    print("WA x " + str(s.count("WA")))
    print("TLE x " + str(s.count("TLE")))
    print("RE x " + str(s.count("RE")))

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ac = s.count('AC')
    wa = s.count('WA')
    tle = s.count('TLE')
    re = s.count('RE')
    print('AC x', ac)
    print('WA x', wa)
    print('TLE x', tle)
    print('RE x', re)

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print('AC x ' + str(S.count('AC')))
    print('WA x ' + str(S.count('WA')))
    print('TLE x ' + str(S.count('TLE')))
    print('RE x ' + str(S.count('RE')))

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    print("AC x {}".format(S.count("AC")))
    print("WA x {}".format(S.count("WA")))
    print("TLE x {}".format(S.count("TLE")))
    print("RE x {}".format(S.count("RE")))

=======
Suggestion 7

def main():
    n = int(input())
    verdicts = []
    for i in range(n):
        verdicts.append(input())
    print('AC x ' + str(verdicts.count('AC')))
    print('WA x ' + str(verdicts.count('WA')))
    print('TLE x ' + str(verdicts.count('TLE')))
    print('RE x ' + str(verdicts.count('RE')))

=======
Suggestion 8

def problem173_b():
    N = int(input())
    verdicts = []
    for i in range(N):
        verdicts.append(input())
    print('AC x', verdicts.count('AC'))
    print('WA x', verdicts.count('WA'))
    print('TLE x', verdicts.count('TLE'))
    print('RE x', verdicts.count('RE'))

=======
Suggestion 9

def main():
    # N = int(input())
    # S = []
    # for i in range(N):
    #     S.append(input())
    N = 6
    S = ['AC', 'TLE', 'AC', 'AC', 'WA', 'TLE']
    C = [0, 0, 0, 0]
    for i in range(N):
        if S[i] == 'AC':
            C[0] += 1
        elif S[i] == 'WA':
            C[1] += 1
        elif S[i] == 'TLE':
            C[2] += 1
        elif S[i] == 'RE':
            C[3] += 1
    print('AC x {}'.format(C[0]))
    print('WA x {}'.format(C[1]))
    print('TLE x {}'.format(C[2]))
    print('RE x {}'.format(C[3]))

=======
Suggestion 10

def main():
    # Take input Here and Call solution function
    n = int(input())
    s = [input() for _ in range(n)]
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))
