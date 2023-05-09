def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',':
            if cnt % 2 == 0:
                print('.', end = '')
            else:
                print(',', end = '')
        else:
            print(s[i], end = '')
    print()

if __name__ == '__main__':
    main()