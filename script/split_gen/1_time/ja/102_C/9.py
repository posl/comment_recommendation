def main():
    N = int(input())
    A = list(map(int, input().split()))
    # b = 1 から N までの値を全探索
    # すべての b についての悲しさの値を計算する
    # 悲しさの値の最小値を出力
    ans = 10**9
    for b in range(1, N+1):
        sad = 0
        for i in range(N):
            sad += abs(A[i] - (b+i))
        ans = min(ans, sad)
    print(ans)
