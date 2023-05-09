def main():
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1) | set(s2) | set(s3)
    if len(chars) > 10:
        print('UNSOLVABLE')
        return
    chars = list(chars)
    for perm in permutations(range(10), len(chars)):
        s1_ = s1
        s2_ = s2
        s3_ = s3
        for i in range(len(chars)):
            s1_ = s1_.replace(chars[i], str(perm[i]))
            s2_ = s2_.replace(chars[i], str(perm[i]))
            s3_ = s3_.replace(chars[i], str(perm[i]))
        if s1_[0] == '0' or s2_[0] == '0' or s3_[0] == '0':
            continue
        if int(s1_) + int(s2_) == int(s3_):
            print(s1_)
            print(s2_)
            print(s3_)
            return
    print('UNSOLVABLE')
from itertools import permutations

if __name__ == '__main__':
    main()