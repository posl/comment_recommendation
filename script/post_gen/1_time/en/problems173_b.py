Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x " + str(s.count("AC")))
    print("WA x " + str(s.count("WA")))
    print("TLE x " + str(s.count("TLE")))
    print("RE x " + str(s.count("RE")))

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print('AC x', s.count('AC'))
    print('WA x', s.count('WA'))
    print('TLE x', s.count('TLE'))
    print('RE x', s.count('RE'))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print("AC x " + str(S.count("AC")))
    print("WA x " + str(S.count("WA")))
    print("TLE x " + str(S.count("TLE")))
    print("RE x " + str(S.count("RE")))

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print('AC x', S.count('AC'))
    print('WA x', S.count('WA'))
    print('TLE x', S.count('TLE'))
    print('RE x', S.count('RE'))

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))

=======
Suggestion 6

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
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    print("AC x", S.count("AC"))
    print("WA x", S.count("WA"))
    print("TLE x", S.count("TLE"))
    print("RE x", S.count("RE"))

=======
Suggestion 8

def main():
    n = int(input())
    verdicts = []
    for i in range(n):
        verdicts.append(input())
    ac = verdicts.count("AC")
    wa = verdicts.count("WA")
    tle = verdicts.count("TLE")
    re = verdicts.count("RE")
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

=======
Suggestion 9

def problem173_b():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x " + str(s.count("AC")))
    print("WA x " + str(s.count("WA")))
    print("TLE x " + str(s.count("TLE")))
    print("RE x " + str(s.count("RE")))
