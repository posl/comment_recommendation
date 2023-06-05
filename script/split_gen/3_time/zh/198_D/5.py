def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s3) or len(s2) > len(s3):
        print("UNSOLVABLE")
        return
    li = list(set(s1 + s2 + s3))
    if len(li) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** len(s1) - 1, 10 ** (len(s1) - 1) - 1, -1):
        for j in range(10 ** len(s2) - 1, 10 ** (len(s2) - 1) - 1, -1):
            if i + j > 10 ** len(s3):
                continue
            s = str(i) + str(j) + str(i + j)
            if len(s) > 10:
                break
            if len(s) < 10:
                s = "0" * (10 - len(s)) + s
            d = {}
            for k in range(len(li)):
                d[li[k]] = s[k]
            if len(set(d.values())) == len(d.values()):
                for k in range(3):
                    for l in range(len(s1)):
                        s1 = s1[:l] + d[s1[l]] + s1[l + 1:]
                    for l in range(len(s2)):
                        s2 = s2[:l] + d[s2[l]] + s2[l + 1:]
                    for l in range(len(s3)):
                        s3 = s3[:l] + d[s3[l]] + s3[l + 1:]
                print(i)
                print(j)
                print(i + j)
                return
    print("UNSOLVABLE")
