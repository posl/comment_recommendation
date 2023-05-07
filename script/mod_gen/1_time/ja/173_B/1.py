def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))

if __name__ == '__main__':
    main()