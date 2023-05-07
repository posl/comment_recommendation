def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ac = s.count("AC")
    wa = s.count("WA")
    tle = s.count("TLE")
    re = s.count("RE")
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

if __name__ == '__main__':
    main()