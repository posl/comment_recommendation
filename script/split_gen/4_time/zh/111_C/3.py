def main():
    n = int(input())
    v = list(map(int,input().split()))
    a = v[0::2]
    b = v[1::2]
    from collections import Counter
    a = Counter(a).most_common(2)
    b = Counter(b).most_common(2)
    if a[0][0] != b[0][0]:
        print(n-a[0][1]-b[0][1])
    else:
        if len(a) == 1 and len(b) == 1:
            print(n//2)
        elif len(a) == 1:
            print(n-b[1][1])
        elif len(b) == 1:
            print(n-a[1][1])
        else:
            print(min(n-a[1][1]-b[0][1],n-a[0][1]-b[1][1]))
