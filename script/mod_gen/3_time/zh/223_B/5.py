def main():
    s = input()
    s = s.strip()
    s = s.lower()
    s = s + s
    s_min = s
    s_max = s
    for i in range(len(s)):
        if s[i:] + s[:i] < s_min:
            s_min = s[i:] + s[:i]
        if s[i:] + s[:i] > s_max:
            s_max = s[i:] + s[:i]
    print(s_min[0:len(s)//2])
    print(s_max[0:len(s)//2])

if __name__ == '__main__':
    main()