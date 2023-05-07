def main():
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[1], reverse=True)
    kinds = set()
    kinds.add(data[0][0])
    ret = data[0][1]
    for i in range(1, K):
        if data[i][0] in kinds:
            ret += data[i][1]
        else:
            kinds.add(data[i][0])
            ret += data[i][1] + len(kinds) * len(kinds)
    for i in range(K, N):
        if data[i][0] in kinds:
            ret = max(ret, data[i][1] + sum(map(lambda x: x[1], filter(lambda x: x[0] in kinds, data[:i]))) + len(kinds) * len(kinds))
        else:
            ret = max(ret, data[i][1] + sum(map(lambda x: x[1], filter(lambda x: x[0] in kinds, data[:i]))) + (len(kinds) + 1) * (len(kinds) + 1))
    print(ret)
