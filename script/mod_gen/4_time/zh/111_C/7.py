def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    v1c = {}
    v2c = {}
    for i in v1:
        if i in v1c:
            v1c[i] += 1
        else:
            v1c[i] = 1
    for i in v2:
        if i in v2c:
            v2c[i] += 1
        else:
            v2c[i] = 1
    v1c = sorted(v1c.items(), key=lambda x: x[1], reverse=True)
    v2c = sorted(v2c.items(), key=lambda x: x[1], reverse=True)
    if v1c[0][0] != v2c[0][0]:
        print(n - v1c[0][1] - v2c[0][1])
    elif len(v1c) == 1 and len(v2c) == 1:
        print(n // 2)
    elif len(v1c) == 1:
        print(n - v1c[0][1] - v2c[1][1])
    elif len(v2c) == 1:
        print(n - v1c[1][1] - v2c[0][1])
    else:
        print(min(n - v1c[0][1] - v2c[1][1], n - v1c[1][1] - v2c[0][1]))

if __name__ == '__main__':
    main()