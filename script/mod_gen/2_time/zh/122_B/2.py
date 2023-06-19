def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            ok = True
            for k in range(i, j + 1):
                if s[k] != 'A' and s[k] != 'C' and s[k] != 'G' and s[k] != 'T':
                    ok = False
            if ok:
                ans = max(ans, j - i + 1)
    print(ans)

if __name__ == '__main__':
    main()