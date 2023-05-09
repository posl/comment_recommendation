def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    if c1.most_common()[0][0] != c2.most_common()[0][0]:
        print(n - c1.most_common()[0][1] - c2.most_common()[0][1])
    else:
        if len(c1) == 1 and len(c2) == 1:
            print(n // 2)
        elif len(c1) == 1:
            print(n - c2.most_common()[1][1])
        elif len(c2) == 1:
            print(n - c1.most_common()[1][1])
        else:
            print(min(n - c1.most_common()[1][1] - c2.most_common()[0][1], n - c1.most_common()[0][1] - c2.most_common()[1][1]))
