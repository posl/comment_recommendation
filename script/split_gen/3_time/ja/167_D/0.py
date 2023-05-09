def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    #print(N, K)
    #print(A)
    #print(A[0])
    # 0 からスタート
    # A[0] に到達したら終了
    # A[0] に到達するまでのループの長さを求める
    # K % ループの長さ だけ進めばよい
    # 現在の位置
    now = 0
    # 通った位置
    route = [0]
    # ループの長さ
    loop = 0
    # ループの開始位置
    loop_start = 0
    while True:
        # 次の位置に移動
        now = A[now]
        # 通った位置に追加
        route.append(now)
        # ループの長さを増やす
        loop += 1
        # 次の位置がループの開始位置と同じになったらループ終了
        if now == route[loop_start]:
            break
        # 次の位置がループの開始位置と同じになるまでループ
        if now == route[loop_start + 1]:
            loop_start += 1
    #print("route:", route)
    #print("loop:", loop)
    #print("loop_start:", loop_start)
    # ループの開始位置を K で割った余りだけループ
    K = K % loop
    #print("K:", K)
    print(route[loop_start + K] + 1)
