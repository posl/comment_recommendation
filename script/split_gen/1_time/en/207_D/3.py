def main():
    n = int(input())
    s, t = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        s.append((x, y))
    for _ in range(n):
        x, y = map(int, input().split())
        t.append((x, y))
    if n == 1:
        print('Yes')
        return
    if n == 2:
        if (s[0][0] - s[1][0]) * (t[0][1] - t[1][1]) == (s[0][1] - s[1][1]) * (t[0][0] - t[1][0]):
            print('Yes')
        else:
            print('No')
        return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    p1 = (s[i][0] - s[j][0], s[i][1] - s[j][1])
                    p2 = (t[i][0] - t[j][0], t[i][1] - t[j][1])
                    p3 = (s[k][0] - s[l][0], s[k][1] - s[l][1])
                    p4 = (t[k][0] - t[l][0], t[k][1] - t[l][1])
                    if p1[0] * p2[1] == p1[1] * p2[0] and p3[0] * p4[1] == p3[1] * p4[0]:
                        print('Yes')
                        return
    print('No')
