def main():
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '+':
            cnt += 1
        else:
            cnt -= 1
    print(cnt)

if __name__ == '__main__':
    main()