def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    i = 0
    while i < s_len:
        if s[i] != t[i]:
            break
        i += 1
    print(i+1)

if __name__ == '__main__':
    main()