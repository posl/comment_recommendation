def main():
    n, m, q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]
    for i in range(q):
        l, r = query[i][0], query[i][1]
        xx = x[:l-1] + x[r:]
        xx.sort()
        res = 0
        for j in range(n):
            for k in range(len(xx)-1, -1, -1):
                if wv[j][0] <= xx[k]:
                    res += wv[j][1]
                    xx.pop(k)
                    break
        print(res)
