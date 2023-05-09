def main():
    # A_i_j の入力
    A = [[0] * 3 for _ in range(3)]
    for i in range(3):
        A[i] = list(map(int, input().split()))
    # N の入力
    N = int(input())
    # b_i の入力
    b = [0] * N
    for i in range(N):
        b[i] = int(input())
    # 3×3 のビンゴカードの初期状態を表す 2 次元配列 B を作成
    B = [[0] * 3 for _ in range(3)]
    # N 個の数 b_1, b_2, ..., b_N が選ばれた時点でビンゴが達成されているかどうかを判定
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if A[j][k] == b[i]:
                    B[j][k] = 1
    # 縦・横・斜めのいずれか 1 列に並んだ 3 つの数の組であって、全てに印の付いているものが存在するかどうかを判定
    # 縦
    for j in range(3):
        if B[0][j] == 1 and B[1][j] == 1 and B[2][j] == 1:
            print('Yes')
            exit()
    # 横
    for i in range(3):
        if B[i][0] == 1 and B[i][1] == 1 and B[i][2] == 1:
            print('Yes')
            exit()
    # 斜め
    if B[0][0] == 1 and B[1][1] == 1 and B[2][2] == 1:
        print('Yes')
        exit()
    if B[0][2] == 1 and B[1][1] == 1 and B[2][0] == 1:
        print('Yes')
        exit()
    #
