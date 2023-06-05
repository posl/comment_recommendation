def main():
    N = int(input())
    S = [input() for i in range(N)]
    print("AC x {}".format(S.count("AC")))
    print("WA x {}".format(S.count("WA")))
    print("TLE x {}".format(S.count("TLE")))
    print("RE x {}".format(S.count("RE")))
main()
