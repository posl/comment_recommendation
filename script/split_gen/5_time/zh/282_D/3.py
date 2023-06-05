def main():
    N, M = map(int, input().split())
    uv = []
    for i in range(M):
        uv.append(list(map(int, input().split())))
    ans = 0
    for i in range(M):
        u = uv[i][0]
        v = uv[i][1]
        for j in range(M):
            if i == j:
                continue
            if uv[j][0] == u and uv[j][1] == v:
                break
        else:
            ans += 1
    print(ans)
