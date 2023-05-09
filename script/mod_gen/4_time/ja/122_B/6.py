def main():
    s = input()
    max_len = 0
    tmp_len = 0
    for c in s:
        if c in "ACGT":
            tmp_len += 1
        else:
            tmp_len = 0
        max_len = max(max_len, tmp_len)
    print(max_len)

if __name__ == '__main__':
    main()