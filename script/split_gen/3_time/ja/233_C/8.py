def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 2^N通りの組み合わせ
    for i in range(2**N):
        # 2進数に変換
        b = format(i, 'b').zfill(N)
        # 組み合わせの積
        sum = 1
        for j in range(N):
            # 組み合わせに含まれる袋の積
            sum *= L[j][int(b[j])+1]
        # 組み合わせの積がXになればカウント
        if sum == X:
            ans += 1
    print(ans)
