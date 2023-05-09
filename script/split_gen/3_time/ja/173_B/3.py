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
