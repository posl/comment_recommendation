def main():
    # N: 参考書の種類数
    # M: アルゴリズムの種類数
    # X: 目標
    N, M, X = map(int, input().split())
    # C: 参考書の値段
    # A: アルゴリズムの理解度
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    # 組み合わせ全探索
    # bit全探索で、参考書を買うか買わないかを全探索
    # それぞれの組み合わせで、アルゴリズムの理解度を計算
    # その中で、X以上のものがあれば、最小値を出力
    # なければ、-1を出力
    ans = 10 ** 10
    for i in range(2 ** N):
        # 2進数に変換
        s = format(i, "b").zfill(N)
        # アルゴリズムの理解度を計算
        # それぞれのアルゴリズムの理解度を0に初期化
        tmp = [0] * M
        # 金額の合計
        money = 0
        for j in range(N):
            if s[j] == "1":
                money += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        # 一つでも理解度がX未満ならば、次のループへ
        if min(tmp) < X:
            continue
        # それ以外ならば、金額の合計を更新
        ans = min(ans, money)
    # -1を出力
    if ans == 10 ** 10:
        print(-1)
    # 最小値を出力
    else:
        print(ans
