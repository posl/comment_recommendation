def main():
    s = input()
    count0 = 0
    count1 = 0
    for i in range(len(s)):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1
    print(min(count0, count1)*2)

if __name__ == '__main__':
    main()