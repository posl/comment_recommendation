def judge():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s3) > 10:
        return False
    if len(s1) + len(s2) != len(s3):
        return False
    s = set()
    for i in range(len(s1)):
        s.add(s1[i])
        s.add(s2[i])
        s.add(s3[i])
    if len(s) > 10:
        return False
    s = list(s)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == 0 and (j == 0 or k == 0):
                    continue
                dic = {}
                for l in range(len(s)):
                    dic[s[l]] = [i, j, k][l]
                n1 = n2 = n3 = 0
                for l in range(len(s1)):
                    n1 = n1 * 10 + dic[s1[l]]
                    n2 = n2 * 10 + dic[s2[l]]
                    n3 = n3 * 10 + dic[s3[l]]
                if n1 + n2 == n3:
                    print(n1)
                    print(n2)
                    print(n3)
                    return True
    return False
