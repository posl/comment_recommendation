def main():
    s = input()
    s_len = len(s)
    count = 0
    index = 0
    while index < s_len:
        if index == 0 and s[index] == '1':
            index += 1
            continue
        if s[index] == '0':
            index += 1
            count += 1
            continue
        if s[index] == '1':
            if index == s_len - 1:
                count += 1
                break
            if s[index + 1] == '0':
                index += 1
                count += 1
                continue
        count += 1
        index += 1
    print(count)

if __name__ == '__main__':
    main()