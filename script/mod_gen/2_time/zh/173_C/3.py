def main():
    N = int(input())
    S = [input() for i in range(N)]
    ac = wa = tle = re = 0
    for i in range(N):
        if S[i] == "AC":
            ac += 1
        elif S[i] == "WA":
            wa += 1
        elif S[i] == "TLE":
            tle += 1
        elif S[i] == "RE":
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

if __name__ == '__main__':
    main()