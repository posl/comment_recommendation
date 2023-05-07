def main():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

if __name__ == '__main__':
    main()