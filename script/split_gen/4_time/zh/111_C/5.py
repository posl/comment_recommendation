def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    from collections import Counter
    c1 = Counter(v1).most_common()
    c2 = Counter(v2).most_common()
    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    elif len(c1) == 1 and len(c2) == 1:
        print(n // 2)
    else:
        print(n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1]))
