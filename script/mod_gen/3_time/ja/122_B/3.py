def main():
    s = input()
    if len(s) == 1:
        if s == 'A' or s == 'C' or s == 'G' or s == 'T':
            print(1)
        else:
            print(0)
    else:
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if 'A' in s[i:j] or 'C' in s[i:j] or 'G' in s[i:j] or 'T' in s[i:j]:
                    if count < len(s[i:j]):
                        count = len(s[i:j])
                else:
                    continue
        print(count)

if __name__ == '__main__':
    main()