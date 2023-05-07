def main():
    h, w, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i)
    for k in d:
        d[k].sort(key=lambda i: b[i])
    ans = [(0, 0)] * n
    for i in range(n):
        ans[i] = (len(d) + 1 - a[i], len(d[a[i]]) + 1 - b[i])
    ans.sort()
    for i in range(n):
        print(ans[i][0], ans[i][1])
