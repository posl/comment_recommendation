def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    ans = -1
    for i in range(1 << n):
        group = []
        for j in range(n):
            if (i >> j) & 1:
                group.append(j)
        if len(group) != n // 2:
            continue
        tmp = 0
        for j in range(n // 2):
            for k in range(j + 1, n // 2):
                tmp += a[group[j]][group[k]]
        ans = max(ans, tmp)
    print(ans)
