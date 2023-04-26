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
        elif s == "RE":
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
        S = str(input())
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
Suggestion 3

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
        else:
            re += 1
    print("AC x", ac)
    print("WA x", wa)
    print("TLE x", tle)
    print("RE x", re)

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    AC = 0
    WA = 0
    TLE = 0
    RE = 0

    for i in range(N):
        if S[i] == "AC":
            AC += 1
        elif S[i] == "WA":
            WA += 1
        elif S[i] == "TLE":
            TLE += 1
        elif S[i] == "RE":
            RE += 1

    print("AC x " + str(AC))
    print("WA x " + str(WA))
    print("TLE x " + str(TLE))
    print("RE x " + str(RE))

=======
Suggestion 5

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    print("AC x", a.count("AC"))
    print("WA x", a.count("WA"))
    print("TLE x", a.count("TLE"))
    print("RE x", a.count("RE"))

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(f"AC x {s.count('AC')}")
    print(f"WA x {s.count('WA')}")
    print(f"TLE x {s.count('TLE')}")
    print(f"RE x {s.count('RE')}")

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    c0 = s.count("AC")
    c1 = s.count("WA")
    c2 = s.count("TLE")
    c3 = s.count("RE")
    print("AC x", c0)
    print("WA x", c1)
    print("TLE x", c2)
    print("RE x", c3)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    print("AC x", S.count("AC"))
    print("WA x", S.count("WA"))
    print("TLE x", S.count("TLE"))
    print("RE x", S.count("RE"))

=======
Suggestion 9

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s_count = [0,0,0,0]
    for i in range(n):
        if s[i] == "AC":
            s_count[0] += 1
        elif s[i] == "WA":
            s_count[1] += 1
        elif s[i] == "TLE":
            s_count[2] += 1
        elif s[i] == "RE":
            s_count[3] += 1
    print("AC x " + str(s_count[0]))
    print("WA x " + str(s_count[1]))
    print("TLE x " + str(s_count[2]))
    print("RE x " + str(s_count[3]))

=======
Suggestion 10

def main():
    #入力
    n = int(input())
    s = [input() for i in range(n)]
    #AC,WA,TLE,REのカウント
    count = [0,0,0,0]
    for i in s:
        if i == "AC":
            count[0] += 1
        elif i == "WA":
            count[1] += 1
        elif i == "TLE":
            count[2] += 1
        elif i == "RE":
            count[3] += 1
    #出力
    print("AC x " + str(count[0]))
    print("WA x " + str(count[1]))
    print("TLE x " + str(count[2]))
    print("RE x " + str(count[3]))
