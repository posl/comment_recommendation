def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()