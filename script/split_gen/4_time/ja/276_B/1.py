def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, A, B)
    # 都市をキーに、道路で直接結ばれた都市を値に持つ辞書を作成する
    cities = {}
    for i in range(M):
        if A[i] not in cities:
            cities[A[i]] = [B[i]]
        else:
            cities[A[i]].append(B[i])
        if B[i] not in cities:
            cities[B[i]] = [A[i]]
        else:
            cities[B[i]].append(A[i])
    #print(cities)
    # 都市の数だけループ
    for i in range(1, N+1):
        # 都市 i と道路で直接結ばれた都市が d_i 個あるとし、それらを昇順に都市 a_{i, 1}, ..., a_{i, d_i} とおく。
        # 都市 i と道路で直接結ばれた都市がない場合
        if i not in cities:
            print(0)
        else:
            # 都市 i と道路で直接結ばれた都市がある場合
            # それらを昇順に都市 a_{i, 1}, ..., a_{i, d_i} とおく。
            print(len(cities[i]), ' '.join(map(str, sorted(cities[i]))))
