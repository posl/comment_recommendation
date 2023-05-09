def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1+S2+S3
    S = set(S)
    if len(S) > 10:
        print('UNSOLVABLE')
        return
    S = list(S)
    for p in permutations(range(10), len(S)):
        S1_ = S1.translate(str.maketrans(dict(zip(S, map(str, p)))))
        S2_ = S2.translate(str.maketrans(dict(zip(S, map(str, p)))))
        S3_ = S3.translate(str.maketrans(dict(zip(S, map(str, p)))))
        if S1_[0] == '0' or S2_[0] == '0' or S3_[0] == '0':
            continue
        if int(S1_) + int(S2_) == int(S3_):
            print(S1_)
            print(S2_)
            print(S3_)
            return
    print('UNSOLVABLE')
