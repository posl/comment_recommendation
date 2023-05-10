def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("Yes" if s.count("For") > n // 2 else "No")

if __name__ == '__main__':
    main()