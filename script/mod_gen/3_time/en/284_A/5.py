def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        print(s[n - i - 1])

if __name__ == '__main__':
    main()