def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print("AC x", S.count("AC"))
    print("WA x", S.count("WA"))
    print("TLE x", S.count("TLE"))
    print("RE x", S.count("RE"))

if __name__ == '__main__':
    main()