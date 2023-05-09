def main():
    s = input()
    cnt = 0
    atcoder = "atcoder"
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()