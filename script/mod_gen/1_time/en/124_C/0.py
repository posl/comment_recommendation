def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '1':
                count += 1
        else:
            if s[i] == '0':
                count += 1
    print(count)

if __name__ == '__main__':
    main()