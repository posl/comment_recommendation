def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    # N個の要素がKのリストを作成
    score_list = [K] * N
    for a in A:
        score_list[a-1] -= 1
    for score in score_list:
        if score > 0:
            print("Yes")
        else:
            print("No")
