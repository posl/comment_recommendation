def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 連続しているボールの個数をカウントする
    cnt = [0] * 200010
    # 1個目のボールを落とす
    cnt[a[0]] += 1
    # 2個目以降のボールを落とす
    for i in range(1, n):
        # 2個目以降のボールを落とす前に、筒の中にあるボールに書かれた整数は下から順に何個あるかを求める
        ans = 0
        for j in range(200010):
            if cnt[j] > 0:
                ans += 1
        # 2個目以降のボールを落とす
        cnt[a[i]] += 1
        # 2個目以降のボールを落とした後、筒の中にあるボールに書かれた整数は下から順に何個あるかを求める
        ans2 = 0
        for j in range(200010):
            if cnt[j] > 0:
                ans2 += 1
        print(ans2 - ans)
