Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("AC x {}".format(s.count("AC")))
    print("WA x {}".format(s.count("WA")))
    print("TLE x {}".format(s.count("TLE")))
    print("RE x {}".format(s.count("RE")))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    AC = S.count("AC")
    WA = S.count("WA")
    TLE = S.count("TLE")
    RE = S.count("RE")
    print("AC x " + str(AC))
    print("WA x " + str(WA))
    print("TLE x " + str(TLE))
    print("RE x " + str(RE))

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print("AC x", S.count("AC"))
    print("WA x", S.count("WA"))
    print("TLE x", S.count("TLE"))
    print("RE x", S.count("RE"))

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print('AC x', S.count('AC'))
    print('WA x', S.count('WA'))
    print('TLE x', S.count('TLE'))
    print('RE x', S.count('RE'))

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    a = S.count('AC')
    b = S.count('WA')
    c = S.count('TLE')
    d = S.count('RE')

    print('AC x ' + str(a))
    print('WA x ' + str(b))
    print('TLE x ' + str(c))
    print('RE x ' + str(d))

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print("AC x {}".format(S.count("AC")))
    print("WA x {}".format(S.count("WA")))
    print("TLE x {}".format(S.count("TLE")))
    print("RE x {}".format(S.count("RE")))

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(n):
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
        elif s[i] == "TLE":
            tle += 1
        elif s[i] == "RE":
            re += 1
    print("AC x {}".format(ac))
    print("WA x {}".format(wa))
    print("TLE x {}".format(tle))
    print("RE x {}".format(re))

=======
Suggestion 9

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    print('AC x', s.count('AC'))
    print('WA x', s.count('WA'))
    print('TLE x', s.count('TLE'))
    print('RE x', s.count('RE'))

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print("AC x {}".format(s.count("AC")))
    print("WA x {}".format(s.count("WA")))
    print("TLE x {}".format(s.count("TLE")))
    print("RE x {}".format(s.count("RE")))
