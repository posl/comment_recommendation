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
    n = int(input())
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(n):
        s = input()
        if s == "AC":
            ac += 1
        elif s == "WA":
            wa += 1
        elif s == "TLE":
            tle += 1
        elif s == "RE":
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

=======
Suggestion 3

def main():
    n = int(input())
    case = [input() for _ in range(n)]
    print('AC x', case.count('AC'))
    print('WA x', case.count('WA'))
    print('TLE x', case.count('TLE'))
    print('RE x', case.count('RE'))

=======
Suggestion 4

def main():
    N = int(input())
    count_AC = 0
    count_WA = 0
    count_TLE = 0
    count_RE = 0
    for i in range(N):
        S = input()
        if S == "AC":
            count_AC += 1
        elif S == "WA":
            count_WA += 1
        elif S == "TLE":
            count_TLE += 1
        elif S == "RE":
            count_RE += 1
    print("AC x " + str(count_AC))
    print("WA x " + str(count_WA))
    print("TLE x " + str(count_TLE))
    print("RE x " + str(count_RE))

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print('AC x', S.count('AC'))
    print('WA x', S.count('WA'))
    print('TLE x', S.count('TLE'))
    print('RE x', S.count('RE'))
main()

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
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
        elif s[i] == "TLE":
            tle += 1
        else:
            re += 1

    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    C = [0, 0, 0, 0]

    for i in range(N):
        if S[i] == "AC":
            C[0] += 1
        elif S[i] == "WA":
            C[1] += 1
        elif S[i] == "TLE":
            C[2] += 1
        elif S[i] == "RE":
            C[3] += 1
        else:
            print("error")

    print("AC x " + str(C[0]))
    print("WA x " + str(C[1]))
    print("TLE x " + str(C[2]))
    print("RE x " + str(C[3]))

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print("AC x {}".format(S.count("AC")))
    print("WA x {}".format(S.count("WA")))
    print("TLE x {}".format(S.count("TLE")))
    print("RE x {}".format(S.count("RE")))

main()
