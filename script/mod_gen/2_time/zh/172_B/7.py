def main():
    s = input()
    t = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()