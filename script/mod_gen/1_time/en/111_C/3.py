def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    c1 = sorted([(v1.count(i), i) for i in set(v1)], reverse=True)
    c2 = sorted([(v2.count(i), i) for i in set(v2)], reverse=True)
    if c1[0][1] != c2[0][1]:
        print(n - c1[0][0] - c2[0][0])
    else:
        print(min(n - c1[0][0] - c2[1][0], n - c1[1][0] - c2[0][0]))

if __name__ == '__main__':
    main()