def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    chars = set(S1 + S2 + S3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    for perm in permutations(range(10), len(chars)):
        table = {ch: d for ch, d in zip(chars, perm)}
        if table[S1[0]] == 0 or table[S2[0]] == 0 or table[S3[0]] == 0:
            continue
        N1 = int("".join([str(table[ch]) for ch in S1]))
        N2 = int("".join([str(table[ch]) for ch in S2]))
        N3 = int("".join([str(table[ch]) for ch in S3]))
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return
    print("UNSOLVABLE")
