def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if 'A' not in s[i:j+1] and 'C' not in s[i:j+1] and 'G' not in s[i:j+1] and 'T' not in s[i:j+1]:
                break
            else:
                max_len = max(max_len, j - i + 1)
    print(max_len)

if __name__ == '__main__':
    main()