def main():
    s = input()
    k = int(input())
    s_len = len(s)
    count = 0
    for i in range(s_len):
        if s[i] == "X":
            count += 1
    if count == s_len:
        print(s_len)
        return
    if k == 0:
        count = 0
        max_count = 0
        for i in range(s_len):
            if s[i] == ".":
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1
        max_count = max(max_count, count)
        print(max_count)
        return
    count = 0
    max_count = 0
    for i in range(s_len):
        if s[i] == ".":
            max_count = max(max_count, count)
            count = 0
        else:
            count += 1
    max_count = max(max_count, count)
    print(max_count + k)

if __name__ == '__main__':
    main()