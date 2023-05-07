def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = Counter(v1)
    c2 = Counter(v2)
    t1 = c1.most_common()
    t2 = c2.most_common()
    if t1[0][0] != t2[0][0]:
        print(n - t1[0][1] - t2[0][1])
    else:
        if len(t1) == 1:
            print(n - t2[1][1])
        elif len(t2) == 1:
            print(n - t1[1][1])
        else:
            print(n - max(t1[0][1] + t2[1][1], t1[1][1] + t2[0][1]))

if __name__ == '__main__':
    main()