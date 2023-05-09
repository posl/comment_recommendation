def main():
    n = int(input())
    v = list(map(int,input().split()))
    n = len(v)
    a = v[0:n:2]
    b = v[1:n:2]
    from collections import Counter
    c1 = Counter(a)
    c2 = Counter(b)
    c1 = sorted(c1.items(), key=lambda x:x[1], reverse=True)
    c2 = sorted(c2.items(), key=lambda x:x[1], reverse=True)
    if c1[0][0] != c2[0][0]:
        print(n - c1[0][1] - c2[0][1])
    else:
        if len(c1) == 1 and len(c2) == 1:
            print(n//2)
        elif len(c1) == 1:
            print(n - c1[0][1] - c2[1][1])
        elif len(c2) == 1:
            print(n - c1[1][1] - c2[0][1])
        else:
            print(n - max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1]))

if __name__ == '__main__':
    main()