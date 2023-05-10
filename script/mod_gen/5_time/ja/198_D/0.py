def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    if len(s1) == 1 and len(s2) == 1 and len(s3) == 1:
        print("0\n0\n0")
        return
    alp = set(s1) | set(s2) | set(s3)
    if len(alp) > 10:
        print("UNSOLVABLE")
        return
    alp = list(alp)
    alp.sort()
    for p in permutations(range(10), len(alp)):
        d = dict(zip(alp, p))
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = 0
        for i in range(len(s1)):
            n1 = n1 * 10 + d[s1[i]]
        n2 = 0
        for i in range(len(s2)):
            n2 = n2 * 10 + d[s2[i]]
        n3 = 0
        for i in range(len(s3)):
            n3 = n3 * 10 + d[s3[i]]
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
    return

if __name__ == '__main__':
    main()