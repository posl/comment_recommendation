def main():
    n = int(input())
    verdicts = []
    for i in range(n):
        verdicts.append(input())
    ac = verdicts.count("AC")
    wa = verdicts.count("WA")
    tle = verdicts.count("TLE")
    re = verdicts.count("RE")
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))
