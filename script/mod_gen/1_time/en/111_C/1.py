def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[::2]
    v2 = v[1::2]
    v1.sort()
    v2.sort()
    if v1[0] == v1[-1]:
        if v2[0] == v2[-1]:
            print(n//2)
        else:
            print(n//2 - v2.count(v2[0]))
    else:
        if v2[0] == v2[-1]:
            print(n//2 - v1.count(v1[0]))
        else:
            print(min(n//2 - v1.count(v1[0]), n//2 - v2.count(v2[0])))

if __name__ == '__main__':
    main()