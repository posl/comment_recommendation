def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        print("UNSOLVABLE")
        return
    for i in range(10**(len(s1)-1), 10**len(s1)):
        if len(set(str(i))) != len(str(i)):
            continue
        for j in range(10**(len(s2)-1), 10**len(s2)):
            if len(set(str(j))) != len(str(j)):
                continue
            if i + j == int(s3):
                d1 = {}
                d2 = {}
                for k in range(len(s1)):
                    d1[s1[k]] = str(i)[k]
                for k in range(len(s2)):
                    d2[s2[k]] = str(j)[k]
                if len(d1) != len(d2):
                    continue
                for k in range(len(s3)):
                    if s3[k] in d1.keys():
                        if d1[s3[k]] != str(i)[k]:
                            break
                    if s3[k] in d2.keys():
                        if d2[s3[k]] != str(j)[k]:
                            break
                else:
                    print(i)
                    print(j)
                    print(s3)
                    return
    else:
        print("UNSOLVABLE")

if __name__ == '__main__':
    main()