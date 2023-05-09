def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    # Aの左上の値をBの左上の値で割った余りを求める
    rem = B[0][0] % 7
    # Aの左上の値をBの左上の値で引いた値を求める
    sub = B[0][0] - 1
    for i in range(N):
        for j in range(M):
            # Aの(i,j)の値をBの左上の値で割った余りとBの(i,j)の値の割った余りが一致しない場合はNo
            if (B[i][j] - sub) % 7 != rem:
                print('No')
                return
    print('Yes')
