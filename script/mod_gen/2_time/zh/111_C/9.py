def main():
    n = int(input())
    v = list(map(int, input().split()))
    v0 = v[::2]
    v1 = v[1::2]
    from collections import Counter
    c0 = Counter(v0)
    c1 = Counter(v1)
    if c0.most_common()[0][0] != c1.most_common()[0][0]:
        print(n - c0.most_common()[0][1] - c1.most_common()[0][1])
    else:
        if len(c0) == 1:
            print(n // 2)
        else:
            c0.most_common()[1][1] = 0
            c1.most_common()[1][1] = 0
            print(n - max(c0.most_common()[1][1] + c1.most_common()[0][1], c0.most_common()[0][1] + c1.most_common()[1][1]))
    return

if __name__ == '__main__':
    main()