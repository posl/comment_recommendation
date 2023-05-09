def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    
    # 1, 2, ..., N の順列を作る
    p = list(range(1, N + 1))
    
    # 順列をひとつずつ調べる
    while True:
        # 順列 p で、A と C が同じ形になっているかを調べる
        ok = True
        for i in range(M):
            # A[i] と B[i] がひもで繋がれているか
            if p[A[i] - 1] == B[i]:
                # C[i] と D[i] がひもで繋がれているか
                if p[C[i] - 1] != D[i]:
                    ok = False
                    break
            # B[i] と A[i] がひもで繋がれているか
            if p[B[i] - 1] == A[i]:
                # D[i] と C[i] がひもで繋がれているか
                if p[D[i] - 1] != C[i]:
                    ok = False
                    break
        # 同じ形になっているなら Yes を出力して終了
        if ok:
            print('Yes')
            return
        
        # 次の順列を作る
        i = N - 1
        while i > 0 and p[i - 1] >= p[i]:
            i -= 1
        if i <= 0:
            break
        j = N - 1
        while p[j] <= p[i - 1]:
            j -= 1
        p[i - 1], p[j] = p[j], p
