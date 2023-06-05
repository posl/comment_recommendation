def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    min_change = t_len
    for i in range(s_len - t_len + 1):
        change = 0
        for j in range(t_len):
            if s[i + j] != t[j]:
                change += 1
        if change < min_change:
            min_change = change
    print(min_change)

if __name__ == '__main__':
    main()