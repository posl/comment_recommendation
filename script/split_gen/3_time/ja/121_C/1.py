def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # AとBを結合して、Aの昇順、Bの昇順にソートする。
    AB = sorted(zip(A, B))
    # print(AB)
    # 合計金額
    total = 0
    # 購入済みの本数
    count = 0
    for a, b in AB:
        if count + b < M:
            total += a * b
            count += b
        else:
            total += a * (M - count)
            break
    print(total)
