def main():
    n = int(input())
    a = [input() for _ in range(n)]
    print("AC x", a.count("AC"))
    print("WA x", a.count("WA"))
    print("TLE x", a.count("TLE"))
    print("RE x", a.count("RE"))

if __name__ == '__main__':
    main()