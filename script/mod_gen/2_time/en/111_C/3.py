def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1.sort()
    v2.sort()
    if v1[0] != v1[-1] and v2[0] != v2[-1]:
        if v1[0] == v2[-1] and v1[-1] == v2[0]:
            print(min(v1.count(v1[0]), v1.count(v1[-1]), v2.count(v2[0]), v2.count(v2[-1])))
        else:
            print(n - max(v1.count(v1[0]), v1.count(v1[-1]), v2.count(v2[0]), v2.count(v2[-1])))
    elif v1[0] == v1[-1] and v2[0] != v2[-1]:
        print(n - v1.count(v1[0]))
    elif v1[0] != v1[-1] and v2[0] == v2[-1]:
        print(n - v2.count(v2[0]))
    else:
        print(n // 2)

if __name__ == '__main__':
    main()