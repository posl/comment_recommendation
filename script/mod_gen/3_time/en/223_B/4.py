def main():
    s = input()
    s_len = len(s)
    s_min = s
    s_max = s
    for i in range(1, s_len):
        s_shift = s[i:] + s[:i]
        if s_shift < s_min:
            s_min = s_shift
        if s_shift > s_max:
            s_max = s_shift
    print(s_min)
    print(s_max)

if __name__ == '__main__':
    main()