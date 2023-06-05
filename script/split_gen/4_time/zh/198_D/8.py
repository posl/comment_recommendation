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
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            k = i + j
            if len(str(k)) != len(s3):
                continue
            d = {}
            for m in range(len(s1)):
                if s1[m] not in d:
                    d[s1[m]] = str(i)[m]
                elif d[s1[m]] != str(i)[m]:
                    break
            else:
                for m in range(len(s2)):
                    if s2[m] not in d:
                        d[s2[m]] = str(j)[m]
                    elif d[s2[m]] != str(j)[m]:
                        break
                else:
                    for m in range(len(s3)):
                        if s3[m] not in d:
                            d[s3[m]] = str(k)[m]
                        elif d[s3[m]] != str(k)[m]:
                            break
                    else:
                        print(i)
                        print(j)
                        print(k)
                        return
    else:
        print("UNSOLVABLE")
