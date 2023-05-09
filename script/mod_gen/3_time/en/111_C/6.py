def main():
    n = int(input())
    v = list(map(int, input().split()))
    #print(v)
    v1 = v[::2]
    v2 = v[1::2]
    #print(v1)
    #print(v2)
    v1.sort()
    v2.sort()
    #print(v1)
    #print(v2)
    v1c = [0] * (10 ** 5 + 1)
    v2c = [0] * (10 ** 5 + 1)
    for i in range(n):
        if i % 2 == 0:
            v1c[v1[i]] += 1
        else:
            v2c[v2[i]] += 1
    #print(v1c)
    #print(v2c)
    v1m = v1c.index(max(v1c))
    v2m = v2c.index(max(v2c))
    #print(v1m)
    #print(v2m)
    if v1m == v2m:
        v1m2 = v1c.index(sorted(v1c, reverse = True)[1])
        v2m2 = v2c.index(sorted(v2c, reverse = True)[1])
        if v1c[v1m] + v2c[v2m2] > v1c[v1m2] + v2c[v2m]:
            print(n - v1c[v1m] - v2c[v2m2])
        else:
            print(n - v1c[v1m2] - v2c[v2m])
    else:
        print(n - v1c[v1m] - v2c[v2m])

if __name__ == '__main__':
    main()