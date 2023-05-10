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

if __name__ == '__main__':
    main()