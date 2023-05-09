def main():
    N = int(input())
    S = [input() for i in range(N)]
    print("AC x " + str(S.count("AC")))
    print("WA x " + str(S.count("WA")))
    print("TLE x " + str(S.count("TLE")))
    print("RE x " + str(S.count("RE")))
