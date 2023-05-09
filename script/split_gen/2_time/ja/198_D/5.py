def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1 + S2 + S3
    S = set(S)
    L = len(S)
    if L > 10:
        print("UNSOLVABLE")
        return
    from itertools import permutations
    for p in permutations(range(10), L):
        d = dict(zip(S, p))
        if d[S1[0]] == 0 or d[S2[0]] == 0 or d[S3[0]] == 0:
            continue
        if int(S1.translate(str.maketrans(d))) + int(S2.translate(str.maketrans(d))) == int(S3.translate(str.maketrans(d))):
            print(int(S1.translate(str.maketrans(d))))
            print(int(S2.translate(str.maketrans(d))))
            print(int(S3.translate(str.maketrans(d))))
            return
    print("UNSOLVABLE")
