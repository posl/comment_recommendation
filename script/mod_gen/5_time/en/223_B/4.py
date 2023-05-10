def main():
    s = input()
    n = len(s)
    s1 = s
    s2 = s
    for i in range(n):
        s1 = s1[1:] + s1[0]
        s2 = s2[-1] + s2[:-1]
        if s1 < s2:
            print(s1)
            print(s2)
            break
    else:
        print(s1)
        print(s2)

if __name__ == '__main__':
    main()