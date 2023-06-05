def main():
    n, a, b = map(int, input().split())
    s = input()
    if a < b:
        print(sum([a if s[i] == s[n - i - 1] else b for i in range(n // 2)]))
    else:
        print(sum([b if s[i] == s[n - i - 1] else a for i in range(n // 2)]))

if __name__ == '__main__':
    main()