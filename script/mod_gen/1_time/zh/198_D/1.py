def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    s = set()
    for c in s1:
        s.add(c)
    for c in s2:
        s.add(c)
    for c in s3:
        s.add(c)
    if len(s) > 10:
        print("UNSOLVABLE")
        return
    l = list(s)
    l.sort()
    if len(l) == 1:
        print(0)
        print(0)
        print(0)
        return
    n = len(l)
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i == j or i == k or j == k:
                    continue
                d = {}
                for m in range(0, n):
                    d[l[m]] = -1
                d[s1[0]] = i
                d[s2[0]] = j
                d[s3[0]] = k
                if d[s1[0]] == 0 and len(s1) > 1:
                    continue
                if d[s2[0]] == 0 and len(s2) > 1:
                    continue
                if d[s3[0]] == 0 and len(s3) > 1:
                    continue
                if d[s1[0]] == -1 or d[s2[0]] == -1 or d[s3[0]] == -1:
                    continue
                n1 = 0
                n2 = 0
                n3 = 0
                for m in range(0, len(s1)):
                    n1 = n1 * 10 + d[s1[m]]
                for m in range(0, len(s2)):
                    n2 = n2 * 10 + d[s2[m]]
                for m in range(0, len(s3)):
                    n3 = n3 * 10 + d[s3[m]]
                if n1 + n2 == n3:
                    print(n1)
                    print(n2)
                    print(n3)
                    return

if __name__ == '__main__':
    main()