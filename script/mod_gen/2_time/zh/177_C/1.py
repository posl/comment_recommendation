def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    min_change = len_t
    for i in range(len_s - len_t + 1):
        change = 0
        for j in range(len_t):
            if s[i + j] != t[j]:
                change += 1
        if change < min_change:
            min_change = change
    print(min_change)

if __name__ == '__main__':
    main()