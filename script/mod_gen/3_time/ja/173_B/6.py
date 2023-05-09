def main():
    n = int(input())
    s = [input() for _ in range(n)]
    c0 = s.count("AC")
    c1 = s.count("WA")
    c2 = s.count("TLE")
    c3 = s.count("RE")
    print("AC x", c0)
    print("WA x", c1)
    print("TLE x", c2)
    print("RE x", c3)

if __name__ == '__main__':
    main()