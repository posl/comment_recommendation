def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(f"AC x {s.count('AC')}")
    print(f"WA x {s.count('WA')}")
    print(f"TLE x {s.count('TLE')}")
    print(f"RE x {s.count('RE')}")

if __name__ == '__main__':
    main()