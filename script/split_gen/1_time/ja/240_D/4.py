def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 筒の中にあるボールの個数
    cnt = 0
    # 筒の中にあるボールの個数を記録する配列
    ans = []
    for i in range(N):
        # 筒の中にあるボールの個数を記録する配列に追加
        ans.append(cnt)
        # 筒の中にあるボールの個数を更新
        if cnt == 0:
            cnt = 1
        else:
            if A[i] == A[i-1]:
                cnt += 1
            else:
                cnt = 1
        # 筒の中にあるボールの個数が2の倍数の時、ボールを消す
        if cnt % 2 == 0:
            cnt -= 2
    # 筒の中にあるボールの個数を記録する配列に追加
    ans.append(cnt)
    # 筒の中にあるボールの個数を出力
    for i in range(N+1):
        print(ans[i])
