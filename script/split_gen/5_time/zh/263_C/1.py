def main():
    N, M = map(int, input().split())
    res = []
    for i in range(1, M + 1):
        res.append([i])
    for i in range(2, N + 1):
        res2 = []
        for j in range(len(res)):
            for k in range(res[j][-1] + 1, M + 1):
                res2.append(res[j] + [k])
        res = res2
    for i in range(len(res)):
        print(' '.join(map(str, res[i])))
