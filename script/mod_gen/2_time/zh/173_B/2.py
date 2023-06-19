def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("AC x {}".format(s.count("AC")))
    print("WA x {}".format(s.count("WA")))
    print("TLE x {}".format(s.count("TLE")))
    print("RE x {}".format(s.count("RE")))

if __name__ == '__main__':
    main()