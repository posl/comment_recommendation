def main():
    s = input()
    acgt = 'ACGT'
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] in acgt:
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

if __name__ == '__main__':
    main()