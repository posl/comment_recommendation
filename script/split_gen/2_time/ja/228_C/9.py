def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 3日目の合計点を計算
    sum3 = [sum(p) for p in P]
    # 4日目の合計点の上位 K 位までを求める
    sum4 = sorted([sum(p) for p in P], reverse=True)[:K]
    for i in range(N):
        # 4日目の合計点が上位 K 位に入る場合
        if sum3[i] + 300 in sum4:
            print("Yes")
        # 4日目の合計点が上位 K 位に入らない場合
        else:
            # 3日目の合計点が上位 K 位に入る場合
            if sum3[i] in sum4:
                # 3日目の合計点が上位 K 位に入るが、4日目の合計点が上位 K 位に入らない場合
                if sum3[i] + 300 not in sum4:
                    print("Yes")
                # 3日目の合計点が上位 K 位に入るが、4日目の合計点が上位 K 位に入る場合
                else:
                    print("No")
            # 3日目の合計点が上位 K 位に入らない場合
            else:
                print("No")
