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
    for i in range(10 ** len(s1)):
        for j in range(10 ** len(s2)):
            if i + j == int(s3):
                n1 = str(i)
                n2 = str(j)
                while len(n1) < len(s1):
                    n1 = "0" + n1
                while len(n2) < len(s2):
                    n2 = "0" + n2
                for k in range(len(s1)):
                    if s1[k] == "?":
                        continue
                    if s1[k] != n1[k]:
                        break
                else:
                    for k in range(len(s2)):
                        if s2[k] == "?":
                            continue
                        if s2[k] != n2[k]:
                            break
                    else:
                        print(i)
                        print(j)
                        print(i + j)
                        return
    print("UNSOLVABLE")

if __name__ == '__main__':
    main()