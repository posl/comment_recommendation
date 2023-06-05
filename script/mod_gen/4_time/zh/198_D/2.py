def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) + len(s2) != len(s3):
        print("UNSOLVABLE")
        return
    m = {}
    for i in range(len(s1)):
        if s1[i] in m:
            if m[s1[i]] != s3[i]:
                print("UNSOLVABLE")
                return
        else:
            m[s1[i]] = s3[i]
    for i in range(len(s2)):
        if s2[i] in m:
            if m[s2[i]] != s3[i + len(s1)]:
                print("UNSOLVABLE")
                return
        else:
            m[s2[i]] = s3[i + len(s1)]
    if len(m) > 10:
        print("UNSOLVABLE")
        return
    m = sorted(m.items(), key=lambda x: x[1])
    if m[0][1] == '0':
        print("UNSOLVABLE")
        return
    for i in range(len(m)):
        print(m[i][1], end="")
    print()

if __name__ == '__main__':
    main()