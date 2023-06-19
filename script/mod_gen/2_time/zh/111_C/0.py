def main():
    n = int(input())
    v = list(map(int,input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    c1_most = c1.most_common(2)
    c2_most = c2.most_common(2)
    if c1_most[0][0] != c2_most[0][0]:
        print(n-c1_most[0][1]-c2_most[0][1])
    elif len(c1_most) == 1 and len(c2_most) == 1:
        print(n//2)
    elif len(c1_most) == 1:
        print(n-c2_most[0][1]-c2_most[1][1])
    elif len(c2_most) == 1:
        print(n-c1_most[0][1]-c1_most[1][1])
    else:
        print(min(n-c1_most[0][1]-c2_most[1][1],n-c1_most[1][1]-c2_most[0][1]))

if __name__ == '__main__':
    main()