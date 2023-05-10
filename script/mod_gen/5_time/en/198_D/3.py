def solve():
    from itertools import permutations
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1+s2+s3)
    if len(chars) > 10:
        print('UNSOLVABLE')
        return
    for perm in permutations(range(10), len(chars)):
        if perm[0] == 0:
            continue
        d = {c: n for c, n in zip(chars, perm)}
        if d[s1[0]] + d[s2[0]] > 9 or d[s3[0]] + d[s3[1]] > 9:
            continue
        n1 = int(''.join(str(d[c]) for c in s1))
        n2 = int(''.join(str(d[c]) for c in s2))
        n3 = int(''.join(str(d[c]) for c in s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')

if __name__ == '__main__':
    solve()