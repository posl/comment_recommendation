def main():
    N, M = map(int, input().split())
    # 都市をkeyとして、都市と直接つながっている都市の数と、直接つながっている都市をvalueとして辞書を作成
    dic = {}
    for i in range(1, N+1):
        dic[i] = [0, []]
    for i in range(M):
        A, B = map(int, input().split())
        dic[A][0] += 1
        dic[B][0] += 1
        dic[A][1].append(B)
        dic[B][1].append(A)
    # 都市と直接つながっている都市をソート
    for i in range(1, N+1):
        dic[i][1].sort()
    # 出力
    for i in range(1, N+1):
        print(dic[i][0], end="")
        for j in dic[i][1]:
            print(" " + str(j), end="")
        print()
