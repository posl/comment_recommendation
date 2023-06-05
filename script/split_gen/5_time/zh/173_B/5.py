def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(n):
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
        elif s[i] == "TLE":
            tle += 1
        else:
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))
