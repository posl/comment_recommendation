def main():
    s = input()
    s0 = s[0] #初期値
    s1 = s[0] #初期値
    for i in range(1,len(s)):
        if i % 2 == 0:
            if s[i] == s0:
                s0 = '0' if s0 == '1' else '1'
        else:
            if s[i] == s1:
                s1 = '0' if s1 == '1' else '1'
    print(min(s.count(s0),s.count(s1)))

if __name__ == '__main__':
    main()