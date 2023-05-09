def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    d1 = {}
    d2 = {}
    for i in range(n//2):
        d1[v1[i]] = d1.get(v1[i], 0) + 1
        d2[v2[i]] = d2.get(v2[i], 0) + 1
    if len(d1) == 1 and len(d2) == 1:
        if v1[0] == v2[0]:
            print(n//2)
        else:
            print(0)
    elif len(d1) == 1 or len(d2) == 1:
        if len(d1) == 1:
            d = d1
        else:
            d = d2
        key = list(d.keys())[0]
        value = d[key]
        print(n//2 - value)
    else:
        key1 = list(d1.keys())[0]
        key2 = list(d2.keys())[0]
        value1 = d1[key1]
        value2 = d2[key2]
        if key1 == key2:
            if value1 > value2:
                print(n//2 - value1)
            else:
                print(n//2 - value2)
        else:
            print(n//2 - value1 - value2)

if __name__ == '__main__':
    main()