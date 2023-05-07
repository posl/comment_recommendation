def main():
    s = input()
    atcoder = "atcoder"
    cnt = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()