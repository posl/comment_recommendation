def solve(n, a):
    from collections import Counter
    a = Counter(a)
    a = sorted(a.items(), key=lambda x: x[0])
    ans = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if a[i][0] != a[j][0] and a[j][0] != a[k][0] and a[i][0] != a[k][0]:
                    ans += a[i][1] * a[j][1] * a[k][1]
    return ans
