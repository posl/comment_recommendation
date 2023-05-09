def main():
    # 標準入力受け取り
    N,M = map(int,input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int,input().split())))
    K = int(input())
    CD = []
    for _ in range(K):
        CD.append(list(map(int,input().split())))
    # bit全探索
    ans = 0
    for i in range(2**K):
        # 皿ごとにボールの数を格納するリスト
        dish = [0] * (N+1)
        # 人ごとにボールを置く皿を決める
        for j in range(K):
            # 人jが皿Cjにボールを置く場合
            if (i>>j)&1:
                dish[CD[j][0]] += 1
            # 人jが皿Djにボールを置く場合
            else:
                dish[CD[j][1]] += 1
        # 条件の数をカウント
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
