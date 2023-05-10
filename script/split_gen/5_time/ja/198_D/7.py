def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    letters = set(s1 + s2 + s3)
    if len(letters) > 10:
        print("UNSOLVABLE")
        return
    letters = list(letters)
    for perm in permutations(range(10), len(letters)):
        d = {c: str(i) for c, i in zip(letters, perm)}
        if all(d[s] != '0' for s in (s1[0], s2[0], s3[0])):
            n1 = int(''.join(d[s] for s in s1))
            n2 = int(''.join(d[s] for s in s2))
            n3 = int(''.join(d[s] for s in s3))
            if n1 + n2 == n3:
                print(n1)
                print(n2)
                print(n3)
                return
    print("UNSOLVABLE")
