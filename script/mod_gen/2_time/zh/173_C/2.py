def main():
    N = int(input())
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(N):
        S = input()
        if S == "AC":
            ac += 1
        elif S == "WA":
            wa += 1
        elif S == "TLE":
            tle += 1
        else:
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

if __name__ == '__main__':
    main()