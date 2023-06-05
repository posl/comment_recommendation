def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s) > 10:
        print('UNSOLVABLE')
        return
    s = list(s)
    for i in range(10-len(s)):
        s.append('')
    s.sort()
    for p in permutations(range(10), len(s)):
        d = {c: p[i] for i, c in enumerate(s)}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int(''.join([str(d[c]) for c in s1]))
        n2 = int(''.join([str(d[c]) for c in s2]))
        n3 = int(''.join([str(d[c]) for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')

if __name__ == '__main__':
    solve()