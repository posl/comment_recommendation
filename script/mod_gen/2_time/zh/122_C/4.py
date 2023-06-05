def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_acgt(s[i:j+1]):
                max_len = max(max_len, j-i+1)
    print(max_len)

if __name__ == '__main__':
    main()