def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        if i % 2 == 0 and s[i] == '1':
            cnt += 1
        elif i % 2 == 1 and s[i] == '0':
            cnt += 1
    print(min(cnt, n-cnt))

if __name__ == '__main__':
    main()