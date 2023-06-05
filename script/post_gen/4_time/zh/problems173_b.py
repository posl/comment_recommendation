Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))

=======
Suggestion 2

def main():
    n = input()
    s = []
    for i in range(int(n)):
        s.append(input())
    print("AC x "+str(s.count("AC")))
    print("WA x "+str(s.count("WA")))
    print("TLE x "+str(s.count("TLE")))
    print("RE x "+str(s.count("RE")))

=======
Suggestion 3

def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('AC x', s.count('AC'))
    print('WA x', s.count('WA'))
    print('TLE x', s.count('TLE'))
    print('RE x', s.count('RE'))

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    c = [s.count('AC'), s.count('WA'), s.count('TLE'), s.count('RE')]
    print('AC x', c[0])
    print('WA x', c[1])
    print('TLE x', c[2])
    print('RE x', c[3])

=======
Suggestion 5

def count_acs(s):
    return s.count('AC')

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
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('AC x', s.count('AC'))
    print('WA x', s.count('WA'))
    print('TLE x', s.count('TLE'))
    print('RE x', s.count('RE'))

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print("AC x {}".format(S.count("AC")))
    print("WA x {}".format(S.count("WA")))
    print("TLE x {}".format(S.count("TLE")))
    print("RE x {}".format(S.count("RE")))

=======
Suggestion 9

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
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
        elif s[i] == "TLE":
            tle += 1
        elif s[i] == "RE":
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))
