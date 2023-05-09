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

if __name__ == '__main__':
    main()