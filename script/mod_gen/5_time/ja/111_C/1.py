def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = [v[i] for i in range(0, n, 2)]
    v2 = [v[i] for i in range(1, n, 2)]
    from collections import Counter
    c1 = Counter(v1)
    c2 = Counter(v2)
    if len(c1) == 1 and len(c2) == 1:
        if c1.most_common()[0][0] == c2.most_common()[0][0]:
            print(n // 2)
        else:
            print(0)
    else:
        a1 = c1.most_common()[0][1]
        a2 = c2.most_common()[0][1]
        if c1.most_common()[0][0] == c2.most_common()[0][0]:
            if len(c1) == 1:
                print(n // 2 - a2)
            elif len(c2) == 1:
                print(n // 2 - a1)
            else:
                print(n - max(a1 + a2, a1 + a2))
        else:
            print(n - a1 - a2)

if __name__ == '__main__':
    main()