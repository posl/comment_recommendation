Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(n):
        s = input()
        if s == 'AC':
            ac += 1
        elif s == 'WA':
            wa += 1
        elif s == 'TLE':
            tle += 1
        elif s == 'RE':
            re += 1
    print('AC x ' + str(ac))
    print('WA x ' + str(wa))
    print('TLE x ' + str(tle))
    print('RE x ' + str(re))

=======
Suggestion 2

def main():
    N = int(input())
    AC = 0
    WA = 0
    TLE = 0
    RE = 0
    for i in range(N):
        S = input()
        if S == "AC":
            AC += 1
        elif S == "WA":
            WA += 1
        elif S == "TLE":
            TLE += 1
        else:
            RE += 1
    print("AC x " + str(AC))
    print("WA x " + str(WA))
    print("TLE x " + str(TLE))
    print("RE x " + str(RE))

=======
Suggestion 3

def main():
    N = int(input())
    AC, WA, TLE, RE = 0, 0, 0, 0
    for i in range(N):
        s = input()
        if s == 'AC':
            AC += 1
        elif s == 'WA':
            WA += 1
        elif s == 'TLE':
            TLE += 1
        elif s == 'RE':
            RE += 1
    print('AC x ' + str(AC))
    print('WA x ' + str(WA))
    print('TLE x ' + str(TLE))
    print('RE x ' + str(RE))

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    N = int(input())
    verdicts = []
    for i in range(N):
        verdicts.append(input())
    AC = verdicts.count("AC")
    WA = verdicts.count("WA")
    TLE = verdicts.count("TLE")
    RE = verdicts.count("RE")
    print("AC x {}".format(AC))
    print("WA x {}".format(WA))
    print("TLE x {}".format(TLE))
    print("RE x {}".format(RE))

main()

=======
Suggestion 6

def main():
    N = int(input())
    verdict = [input() for _ in range(N)]
    print("AC x", verdict.count("AC"))
    print("WA x", verdict.count("WA"))
    print("TLE x", verdict.count("TLE"))
    print("RE x", verdict.count("RE"))

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    N = int(input())
    verdicts = [input() for _ in range(N)]
    verdicts.sort()
    ac = verdicts.count("AC")
    wa = verdicts.count("WA")
    tle = verdicts.count("TLE")
    re = verdicts.count("RE")
    print("AC x", ac)
    print("WA x", wa)
    print("TLE x", tle)
    print("RE x", re)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]

    #compute
    C = [0]*4
    for i in range(N):
        if S[i] == "AC":
            C[0] += 1
        elif S[i] == "WA":
            C[1] += 1
        elif S[i] == "TLE":
            C[2] += 1
        else:
            C[3] += 1

    #output
    print("AC x", C[0])
    print("WA x", C[1])
    print("TLE x", C[2])
    print("RE x", C[3])

=======
Suggestion 10

def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #compute
    C = [0]*4
    for s in S:
        if s == 'AC':
            C[0] += 1
        elif s == 'WA':
            C[1] += 1
        elif s == 'TLE':
            C[2] += 1
        elif s == 'RE':
            C[3] += 1
    #output
    print('AC x', C[0])
    print('WA x', C[1])
    print('TLE x', C[2])
    print('RE x', C[3])
