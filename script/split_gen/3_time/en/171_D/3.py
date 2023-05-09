def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    # カウントする
    count = [0] * (10**5+1)
    for a in A:
        count[a] += 1
    # 累積和をとる
    sum_count = [0] * (10**5+1)
    for i in range(len(count)):
        sum_count[i] = sum_count[i-1] + count[i]
    # 各クエリに対する処理
    for i in range(Q):
        # 値がB[i]の個数を求める
        num = sum_count[C[i]] - sum_count[B[i]-1]
        # C[i]に変換する
        count[B[i]] -= num
        count[C[i]] += num
        # 累積和を更新する
        for j in range(B[i], C[i]+1):
            sum_count[j] = sum_count[j-1] + count[j]
    # 答えを求める
    ans = 0
    for i in range(len(count)):
        ans += i * count[i]
    print(ans)
