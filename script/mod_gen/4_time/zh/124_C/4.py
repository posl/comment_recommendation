def main():
    s = input()
    num = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '1':
                num += 1
        else:
            if s[i] == '0':
                num += 1
    print(num)

if __name__ == '__main__':
    main()