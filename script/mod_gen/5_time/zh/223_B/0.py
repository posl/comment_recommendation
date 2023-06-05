def main():
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        elif s > s_max:
            s_max = s
    print(s_min)
    print(s_max)

if __name__ == '__main__':
    main()