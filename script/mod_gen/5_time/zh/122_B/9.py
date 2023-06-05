def main():
    s = input()
    max_length = 0
    length = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            length += 1
        else:
            length = 0
        max_length = max(max_length, length)
    print(max_length)

if __name__ == '__main__':
    main()