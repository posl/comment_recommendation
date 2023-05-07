def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    #各頂点の次数を格納するリスト
    degree = [0] * (N + 1)
    #各頂点の次数を更新
    for _ in range(M):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
    #各頂点の次数が2であるかチェック
    for i in range(1, N + 1):
        if degree[i] != 2:
            print("No")
            return
    print("Yes")
