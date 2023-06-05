def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    min_count = s_len
    for i in range(s_len - t_len + 1):
        count = 0
        for j in range(t_len):
            if s[i + j] != t[j]:
                count += 1
        if count < min_count:
            min_count = count
    print(min_count)

if __name__ == '__main__':
    main()