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

if __name__ == '__main__':
    main()