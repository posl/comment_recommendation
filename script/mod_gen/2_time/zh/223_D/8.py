def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 逆向きに解く
    # ある数値が出現する回数を数える
    # ある数値より小さい数値の出現回数を数える
    # ある数値より大きい数値の出現回数を数える
    count = [0] * N
    smaller = [0] * N
    bigger = [0] * N
    for i in range(M):
        count[B[i]-1] += 1
        if A[i] < B[i]:
            smaller[B[i]-1] += 1
        if A[i] > B[i]:
            bigger[B[i]-1] += 1
    # 答えを格納する配列
    ans = []
    # ある数値を出現させるかどうかを決める
    # ある数値より小さい数値が出現していない
    # かつ、ある数値より大きい数値が出現していない
    # ある数値より小さい数値の出現回数を減らす
    # ある数値より大きい数値の出現回数を増やす
    for i in range(N):
        if smaller[i] == 0 and bigger[i] == 0:
            ans.append(i+1)
            for j in range(N):
                if smaller[j] > 0:
                    smaller[j] -= 1
                if bigger[j] > 0:
                    bigger[j] += 1
    # 答えを出力する
    if len(ans) == N:
        print(*ans)
    else:
        print(-1)

if __name__ == '__main__':
    solve()