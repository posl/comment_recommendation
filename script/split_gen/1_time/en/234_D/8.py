def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # Pの先頭K個の最大値を求める
    max_list = [max(P[:K])]
    # Pの先頭K個の最大値を除いた残りのリストを作る
    for i in range(N-K):
        P.pop(0)
        max_list.append(max(P[:K]))
    # 結果を表示
    for max_val in max_list:
        print(max_val)
