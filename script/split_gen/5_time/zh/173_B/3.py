def main():
    N = int(input())
    count_AC = 0
    count_WA = 0
    count_TLE = 0
    count_RE = 0
    for i in range(N):
        S = input()
        if S == "AC":
            count_AC += 1
        elif S == "WA":
            count_WA += 1
        elif S == "TLE":
            count_TLE += 1
        elif S == "RE":
            count_RE += 1
    print("AC x " + str(count_AC))
    print("WA x " + str(count_WA))
    print("TLE x " + str(count_TLE))
    print("RE x " + str(count_RE))
