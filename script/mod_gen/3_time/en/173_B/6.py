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

if __name__ == '__main__':
    main()