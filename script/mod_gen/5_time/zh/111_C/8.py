def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    from collections import Counter
    ceven = Counter(even)
    codd = Counter(odd)
    if ceven.most_common()[0][0] != codd.most_common()[0][0]:
        print(n - ceven.most_common()[0][1] - codd.most_common()[0][1])
    else:
        print(min(n - ceven.most_common()[1][1] - codd.most_common()[0][1], n - ceven.most_common()[0][1] - codd.most_common()[1][1]))

if __name__ == '__main__':
    main()