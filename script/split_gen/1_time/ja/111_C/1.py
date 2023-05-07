def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    d1 = {}
    d2 = {}
    for i in v1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    for i in v2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
    d1 = sorted(d1.items(), key=lambda x: -x[1])
    d2 = sorted(d2.items(), key=lambda x: -x[1])
    if d1[0][0] == d2[0][0]:
        if len(d1) == 1 and len(d2) == 1:
            print(n//2)
        elif len(d1) == 1:
            print(n//2 - d2[1][1])
        elif len(d2) == 1:
            print(n//2 - d1[1][1])
        else:
            print(min(n - d1[0][1] - d2[1][1], n - d1[1][1] - d2[0][1]))
    else:
        print(n - d1[0][1] - d2[0][1])
