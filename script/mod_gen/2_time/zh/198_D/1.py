def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s) > 10:
        print('UNSOLVABLE')
        return
    s = list(s)
    s.sort()
    a = [0]*len(s)
    for i in range(len(s)):
        a[i] = i
    while True:
        if a[0] == 0 or a[len(a)-len(s1)] == 0 or a[len(a)-len(s2)] == 0 or a[len(a)-len(s3)] == 0:
            a = next_permutation(a)
            if a is None:
                print('UNSOLVABLE')
                return
            continue
        d = {}
        for i in range(len(s)):
            d[s[i]] = a[i]
        if d[s1[0]] + d[s2[0]] != d[s3[0]]:
            a = next_permutation(a)
            if a is None:
                print('UNSOLVABLE')
                return
            continue
        n1 = 0
        for i in range(len(s1)):
            n1 = n1*10 + d[s1[i]]
        n2 = 0
        for i in range(len(s2)):
            n2 = n2*10 + d[s2[i]]
        n3 = 0
        for i in range(len(s3)):
            n3 = n3*10 + d[s3[i]]
        if n1 + n2 != n3:
            a = next_permutation(a)
            if a is None:
                print('UNSOLVABLE')
                return
            continue
        print(n1)
        print(n2)
        print(n3)
        return

if __name__ == '__main__':
    solve()