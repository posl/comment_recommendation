def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[0::2]
    b = v[1::2]
    from collections import Counter
    a = Counter(a).most_common()
    b = Counter(b).most_common()
    if a[0][0] == b[0][0]:
        if len(a) == 1 and len(b) == 1:
            print(n//2)
        elif len(a) == 1:
            print(n//2 - b[1][1])
        elif len(b) == 1:
            print(n//2 - a[1][1])
        else:
            print(n//2 - max(a[1][1], b[1][1]))
    else:
        print(n//2 - a[0][1] - b[0][1])
