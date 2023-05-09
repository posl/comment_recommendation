def main():
    s = input()
    s = s.strip()
    s = s.lower()
    l = len(s)
    s1 = s
    s2 = s
    for i in range(l):
        s1 = s1[1:] + s1[0]
        s2 = s2[-1] + s2[:-1]
        if s1 < s2:
            print(s1)
            print(s2)
            return
    print(s1)
    print(s2)
    return

if __name__ == '__main__':
    main()