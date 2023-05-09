def main():
    N, K = map(int, input().split())
    T = [None] * N
    D = [None] * N
    for i in range(N):
        t, d = map(int, input().split())
        T[i] = t
        D[i] = d
    # 種類数が多い順にソート
    order = sorted(range(N), key=lambda i: D[i], reverse=True)
    T = [T[i] for i in order]
    D = [D[i] for i in order]
    # 種類数が多い順に K 個を選ぶ
    selected = set()
    selected_d = []
    for i in range(K):
        selected.add(T[i])
        selected_d.append(D[i])
    ans = sum(selected_d) + len(selected) ** 2
    # 種類数が少ない順に残りを選ぶ
    for i in range(K, N):
        if T[i] in selected:
            continue
        else:
            # 一番おいしさが低い寿司を選ぶ
            min_d = min(selected_d)
            if D[i] <= min_d:
                continue
            else:
                selected.remove(T[selected_d.index(min_d)])
                selected.add(T[i])
                selected_d[selected_d.index(min_d)] = D[i]
                ans = max(ans, sum(selected_d) + len(selected) ** 2)
    print(ans)
