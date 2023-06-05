def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    # print(s1, s2, s3)
    # print(len(s1), len(s2), len(s3))
    # print(s1, s2, s3)
    # print(len(s1), len(s2), len(s3))
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** len(s1) - 1, 10 ** (len(s1) - 1) - 1, -1):
        # print(i)
        n1 = str(i)
        if len(n1) != len(s1):
            continue
        flag = True
        for j in range(len(s1)):
            if n1[j] in n1[:j] or n1[j] in n1[j + 1:]:
                flag = False
                break
        if not flag:
            continue
        # print(n1)
        for k in range(10 ** len(s2) - 1, 10 ** (len(s2) - 1) - 1, -1):
            n2 = str(k)
            if len(n2) != len(s2):
                continue
            flag = True
            for j in range(len(s2)):
                if n2[j] in n2[:j] or n2[j] in n2[j + 1:]:
                    flag = False
                    break
            if not flag:
                continue
            # print(n2)
            for l in range(10 ** len(s3) - 1, 10 ** (len(s3) - 1) - 1, -1):
                n3 = str(l)
                if len(n3) != len(s3):

if __name__ == '__main__':
    main()