def main():
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:len(s)] + s[0]
        s_min = min(s_min, s)
        s_max = max(s_max, s)
    print(s_min)
    print(s_max)

if __name__ == '__main__':
    main()