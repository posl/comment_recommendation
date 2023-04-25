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
        if s == "AC":
            ac += 1
        elif s == "WA":
            wa += 1
        elif s == "TLE":
            tle += 1
        else:
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

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
        elif S == "RE":
            RE += 1
    print("AC x " + str(AC))
    print("WA x " + str(WA))
    print("TLE x " + str(TLE))
    print("RE x " + str(RE))

main()

=======
Suggestion 3

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
        elif S == "RE":
            RE += 1
    print("AC x", AC)
    print("WA x", WA)
    print("TLE x", TLE)
    print("RE x", RE)

=======
Suggestion 4

def main():
    n = int(input())
    ac, wa, tle, re = 0, 0, 0, 0
    for i in range(n):
        s = input()
        if s == "AC":
            ac += 1
        elif s == "WA":
            wa += 1
        elif s == "TLE":
            tle += 1
        else:
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

=======
Suggestion 5

def main():
    n = int(input())
    ac, wa, tle, re = 0, 0, 0, 0
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
    print('AC x', ac)
    print('WA x', wa)
    print('TLE x', tle)
    print('RE x', re)

=======
Suggestion 6

def main():
    n = int(input())
    ac = wa = tle = re = 0
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
Suggestion 7

def main():
    N = int(input())
    verdict = [input() for i in range(N)]
    AC = verdict.count("AC")
    WA = verdict.count("WA")
    TLE = verdict.count("TLE")
    RE = verdict.count("RE")
    print("AC x {}".format(AC))
    print("WA x {}".format(WA))
    print("TLE x {}".format(TLE))
    print("RE x {}".format(RE))

=======
Suggestion 8

def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]

    #compute
    C = [0, 0, 0, 0]
    for s in S:
        if s == "AC":
            C[0] += 1
        elif s == "WA":
            C[1] += 1
        elif s == "TLE":
            C[2] += 1
        else:
            C[3] += 1

    #output
    print("AC x " + str(C[0]))
    print("WA x " + str(C[1]))
    print("TLE x " + str(C[2]))
    print("RE x " + str(C[3]))

=======
Suggestion 9

def main():
    n = int(input())
    verdicts = [input() for _ in range(n)]
    verdicts = [verdict for verdict in verdicts if verdict in ['AC', 'WA', 'TLE', 'RE']]
    verdicts = dict((verdict, verdicts.count(verdict)) for verdict in verdicts)
    print('AC x {}'.format(verdicts['AC']))
    print('WA x {}'.format(verdicts['WA']))
    print('TLE x {}'.format(verdicts['TLE']))
    print('RE x {}'.format(verdicts['RE']))

=======
Suggestion 10

def main():
    # Get number of test cases
    numTestCases = int(input())
    # Initialize counters for each verdict
    ac = 0
    wa = 0
    tle = 0
    re = 0
    # Loop through the test cases
    for i in range(0,numTestCases):
        # Get the verdict
        verdict = input()
        # Increment the counter for the corresponding verdict
        if verdict == "AC":
            ac += 1
        elif verdict == "WA":
            wa += 1
        elif verdict == "TLE":
            tle += 1
        elif verdict == "RE":
            re += 1
    # Print the results
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))
