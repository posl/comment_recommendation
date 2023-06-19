def main():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        s = str(i)
        if s[-1] == s[0]:
            cnt += 1
    for i in range(1, n + 1):
        s = str(i)
        if s[-1] != s[0]:
            continue
        for j in range(1, n + 1):
            s = str(j)
            if s[-1] != s[0]:
                continue
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()