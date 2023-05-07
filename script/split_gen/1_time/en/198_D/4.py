def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    if n1 > n3 or n2 > n3:
        print("UNSOLVABLE")
        return
    s = set(s1 + s2 + s3)
    if len(s) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** (n1 - 1), 10 ** n1):
        for j in range(10 ** (n2 - 1), 10 ** n2):
            for k in range(10 ** (n3 - 1), 10 ** n3):
                if i + j == k:
                    si = str(i)
                    sj = str(j)
                    sk = str(k)
                    if len(si) != n1 or len(sj) != n2 or len(sk) != n3:
                        continue
                    flag = True
                    for c in s:
                        if si.count(c) != s1.count(c) or sj.count(c) != s2.count(c) or sk.count(c) != s3.count(c):
                            flag = False
                            break
                    if flag:
                        print(si)
                        print(sj)
                        print(sk)
                        return
    print("UNSOLVABLE")
