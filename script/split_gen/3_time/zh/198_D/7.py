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
    # print(s1, s2, s3)
    if len(s3) > 10:
        print("UNSOLVABLE")
        return
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    # print(s1, s2, s3)
    d = {}
    for i in s1:
        d[i] = -1
    for i in s2:
        d[i] = -1
    for i in s3:
        d[i] = -1
    # print(d)
    if len(d) > 10:
        print("UNSOLVABLE")
        return
    if len(d) == 10:
        for i in range(10):
            d[chr(ord('0')+i)] = i
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            print("UNSOLVABLE")
            return
        n1 = 0
        n2 = 0
        n3 = 0
        for i in range(len(s1)):
            n1 = n1*10 + d[s1[i]]
        for i in range(len(s2)):
            n2 = n2*10 + d[s2[i]]
        for i in range(len(s3)):
            n3 = n3*10 + d[s3[i]]
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
        else:
            print("UNSOLVABLE")
        return
    else:
        for i in range(10):
            d[chr(ord('0')+i)] = i
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            print("
