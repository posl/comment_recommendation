def main():
    N = int(input())
    verdict = [input() for _ in range(N)]
    print("AC x", verdict.count("AC"))
    print("WA x", verdict.count("WA"))
    print("TLE x", verdict.count("TLE"))
    print("RE x", verdict.count("RE"))

if __name__ == '__main__':
    main()