def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_ACGT(s[i:j]):
                max_len = max(max_len, j-i)
    print(max_len)

if __name__ == '__main__':
    main()