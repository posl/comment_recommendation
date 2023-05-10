def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1c = {}
    v2c = {}
    for i in range(n//2):
        if v1[i] in v1c:
            v1c[v1[i]] += 1
        else:
            v1c[v1[i]] = 1
        if v2[i] in v2c:
            v2c[v2[i]] += 1
        else:
            v2c[v2[i]] = 1
    v1c_sorted = sorted(v1c.items(), key=lambda x: x[1], reverse=True)
    v2c_sorted = sorted(v2c.items(), key=lambda x: x[1], reverse=True)
    if v1c_sorted[0][0] == v2c_sorted[0][0]:
        if len(v1c_sorted) == 1 and len(v2c_sorted) == 1:
            print(n // 2)
        elif len(v1c_sorted) == 1:
            print(n // 2 - v2c_sorted[1][1])
        elif len(v2c_sorted) == 1:
            print(n // 2 - v1c_sorted[1][1])
        else:
            print(min(n // 2 - v1c_sorted[1][1] - v2c_sorted[0][1], n // 2 - v1c_sorted[0][1] - v2c_sorted[1][1]))
    else:
        print(n // 2 - v1c_sorted[0][1] - v2c_sorted[0][1])

if __name__ == '__main__':
    main()