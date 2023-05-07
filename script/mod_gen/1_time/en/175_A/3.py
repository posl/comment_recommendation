def main():
    s = input()
    count = 0
    maxCount = 0
    for i in range(len(s)):
        if s[i] == 'R':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if count > maxCount:
        maxCount = count
    print(maxCount)

if __name__ == '__main__':
    main()