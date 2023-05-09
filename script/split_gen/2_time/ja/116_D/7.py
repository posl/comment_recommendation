def main():
    N,K = map(int,input().split())
    sushi = []
    for i in range(N):
        t_i,d_i = map(int,input().split())
        sushi.append([t_i,d_i])
    sushi.sort(key=lambda x:x[1],reverse=True)
    #print(sushi)
    #種類数
    kind = set([sushi[i][0] for i in range(K)])
    #print(kind)
    #種類数のボーナス
    bonus = len(kind)*len(kind)
    #print(bonus)
    #おいしさの合計
    taste = sum([sushi[i][1] for i in range(K)])
    #print(taste)
    #満足度
    satisfaction = bonus + taste
    #print(satisfaction)
    #種類数がK個になるまで、おいしさの低い寿司を交換する
    for i in range(K,N):
        if len(kind) == K:
            break
        if sushi[i][0] in kind:
            continue
        else:
            kind.add(sushi[i][0])
            bonus = len(kind)*len(kind)
            taste -= sushi[i-K][1]
            taste += sushi[i][1]
            satisfaction = max(satisfaction,bonus+taste)
    print(satisfaction)
