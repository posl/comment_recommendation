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
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        n1 = str(i)
        if len(n1) != len(s1):
            continue
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            n2 = str(j)
            if len(n2) != len(s2):
                continue
            n3 = str(i + j)
            if len(n3) != len(s3):
                continue
            d = {}
            for k in range(len(s1)):
                if s1[k] not in d:
                    d[s1[k]] = n1[k]
                elif d[s1[k]] != n1[k]:
                    break
            else:
                for k in range(len(s2)):
                    if s2[k] not in d:
                        d[s2[k]] = n2[k]
                    elif d[s2[k]] != n2[k]:
                        break
                else:
                    for k in range(len(s3)):
                        if s3[k] not in d:
                            d[s3[k]] = n3[k]
                        elif d[s3[k]] != n3[k]:
                            break
                    else:
                        print(i)
                        print(j)
                        print(i + j)
                        return
    print("UNSOLVABLE")
