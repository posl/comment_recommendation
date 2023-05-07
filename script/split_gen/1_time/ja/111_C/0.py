def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    c1_max = c1.most_common(1)[0]
    c2_max = c2.most_common(1)[0]
    if c1_max[0] != c2_max[0]:
        print(n - c1_max[1] - c2_max[1])
    else:
        # 1種類の数が最大値になる場合
        if len(c1) == 1 and len(c2) == 1:
            print(n // 2)
        # 2種類の数が最大値になる場合
        else:
            c1_max2 = c1.most_common(2)[1]
            c2_max2 = c2.most_common(2)[1]
            print(n - max(c1_max[1] + c2_max2[1], c1_max2[1] + c2_max[1]))
