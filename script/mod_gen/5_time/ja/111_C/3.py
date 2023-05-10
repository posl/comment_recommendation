def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = []
    v2 = []
    for i in range(n):
        if i % 2 == 0:
            v1.append(v[i])
        else:
            v2.append(v[i])
    v1_count = [v1.count(i) for i in set(v1)]
    v2_count = [v2.count(i) for i in set(v2)]
    if len(set(v1)) == 1 and len(set(v2)) == 1:
        if v1[0] == v2[0]:
            print(n // 2)
        else:
            print(0)
    elif len(set(v1)) == 1:
        if v1[0] == v2[0]:
            print(n // 2)
        else:
            print(n // 2 - v2_count[0])
    elif len(set(v2)) == 1:
        if v1[0] == v2[0]:
            print(n // 2)
        else:
            print(n // 2 - v1_count[0])
    else:
        print(n - max(v1_count) - max(v2_count))

if __name__ == '__main__':
    main()