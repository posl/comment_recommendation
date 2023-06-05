def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    # 二分探索
    def is_ok(k):
        # k 分内にクリアできるステージ数
        # k 分内にクリアできるステージの回数
        cnt = 0
        for i in range(N):
            # 難易度が A[i] であるステージを k 分以内にクリアできるか？
            # k 分以内にステージをクリアできる場合
            if k - A[i] >= 0:
                # k - A[i] 分以内に B[i] 回クリアできる
                cnt += (k - A[i]) // B[i] + 1
            # k 分以内にステージをクリアできない場合
            else:
                # 何もしない
                pass
        # k 分以内にクリアできるステージの回数が X 回以上である場合
        if cnt >= X:
            return True
        # k 分以内にクリアできるステージの回数が X 回未満である場合
        else:
            return False
    # 二分探索
    # left は is_ok が True を返す最小の入力値-1
    # right は is_ok が False を返す最大の入力値+1
    left = -1
    right = 10 ** 18
    while right - left > 1:
        mid = left + (right - left) // 2
        # mid 分以内にクリアできるステージの回数が X 回以上である場合
        if is_ok(mid):
            right = mid
        # mid 分以内にクリアできるステージの回数が

if __name__ == '__main__':
    solve()