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
