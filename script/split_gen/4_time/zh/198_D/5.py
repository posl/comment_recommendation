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
        print('UNSOLVABLE')
        return
    for i in range(10**(len(s3)-len(s1)), 10**(len(s3)-len(s1)+1)):
        s1d = str(i)
        if len(s1d) != len(s1):
            continue
        s2d = str(i * 2)
        if len(s2d) != len(s2):
            continue
        s3d = str(i * 3)
        if len(s3d) != len(s3):
            continue
        d = {}
        for j in range(len(s1d)):
            if s1[j] in d:
                if d[s1[j]] != s1d[j]:
                    break
            else:
                d[s1[j]] = s1d[j]
        else:
            for j in range(len(s2d)):
                if s2[j] in d:
                    if d[s2[j]] != s2d[j]:
                        break
                else:
                    d[s2[j]] = s2d[j]
            else:
                for j in range(len(s3d)):
                    if s3[j] in d:
                        if d[s3[j]] != s3d[j]:
                            break
                    else:
                        d[s3[j]] = s3d[j]
                else:
                    print(s1d)
                    print(s2d)
                    print(s3d)
                    return
    print('UNSOLVABLE')
    return
