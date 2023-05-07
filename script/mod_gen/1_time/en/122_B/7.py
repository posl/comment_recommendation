def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if s[i:j + 1].count("A") * s[i:j + 1].count("C") * s[i:j + 1].count("G") * s[i:j + 1].count("T") != 0:
                ans = max(ans, j - i + 1)
    print(ans)

if __name__ == '__main__':
    main()