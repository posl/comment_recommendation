def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1+s2+s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    for p in permutations(range(10), len(chars)):
        d = {}
        for i in range(len(chars)):
            d[chars[i]] = p[i]
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = 0
        n2 = 0
        n3 = 0
        for i in range(len(s1)):
            n1 *= 10
            n1 += d[s1[i]]
        for i in range(len(s2)):
            n2 *= 10
            n2 += d[s2[i]]
        for i in range(len(s3)):
            n3 *= 10
            n3 += d[s3[i]]
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
    return
from itertools import permutations
solve()

if __name__ == '__main__':
    solve()