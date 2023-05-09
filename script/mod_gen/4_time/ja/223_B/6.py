def main():
    s = input()
    min_str = s
    max_str = s
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if min_str > tmp:
            min_str = tmp
        if max_str < tmp:
            max_str = tmp
    print(min_str)
    print(max_str)

if __name__ == '__main__':
    main()