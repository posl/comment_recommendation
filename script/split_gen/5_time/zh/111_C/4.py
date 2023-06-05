def main():
    n = int(input())
    a = list(map(int, input().split()))
    a1 = a[0::2]
    a2 = a[1::2]
    from collections import Counter
    c1 = Counter(a1).most_common(2)
    c2 = Counter(a2).most_common(2)
    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    elif len(c1) == 1 and len(c2) == 1:
        print(n // 2)
    else:
        print(n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1]))
