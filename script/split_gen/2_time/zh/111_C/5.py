def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    c1 = [v1.count(i) for i in set(v1)]
    c2 = [v2.count(i) for i in set(v2)]
    if len(set(v1)) == 1 and len(set(v2)) == 1:
        if v1[0] == v2[0]:
            print(n//2)
        else:
            print(0)
    elif len(set(v1)) == 1 and len(set(v2)) != 1:
        if v1[0] == v2[c2.index(max(c2))]:
            print(n//2 - max(c2))
        else:
            print(n//2 - max(c2) - 1)
    elif len(set(v1)) != 1 and len(set(v2)) == 1:
        if v2[0] == v1[c1.index(max(c1))]:
            print(n//2 - max(c1))
        else:
            print(n//2 - max(c1) - 1)
    else:
        if v1[c1.index(max(c1))] == v2[c2.index(max(c2))]:
            c1[c1.index(max(c1))] = 0
            c2[c2.index(max(c2))] = 0
            if max(c1) > max(c2):
                print(n//2 - max(c1) - max(c2))
            else:
                print(n//2 - max(c1) - max(c2) - 1)
        else:
            print(n//2 - max(c1) - max(c2))
main()
