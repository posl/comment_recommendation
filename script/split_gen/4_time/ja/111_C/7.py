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
    d1_sorted = sorted(d1.items(), key=lambda x: x[1], reverse=True)
    d2_sorted = sorted(d2.items(), key=lambda x: x[1], reverse=True)
    if d1_sorted[0][0] != d2_sorted[0][0]:
        print(n - d1_sorted[0][1] - d2_sorted[0][1])
    else:
        if len(d1_sorted) == 1 and len(d2_sorted) == 1:
            print(n//2)
        elif len(d1_sorted) == 1:
            print(n - d1_sorted[0][1] - d2_sorted[1][1])
        elif len(d2_sorted) == 1:
            print(n - d1_sorted[1][1] - d2_sorted[0][1])
        else:
            print(min(n - d1_sorted[0][1] - d2_sorted[1][1], n - d1_sorted[1][1] - d2_sorted[0][1]))
