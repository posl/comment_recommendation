def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    #各生徒の合計点を求める
    #N個の要素を持つ配列を用意
    total = [0] * N
    for i in range(N):
        total[i] = sum(P[i])
    #合計点をソートする
    total.sort()
    #各生徒の合計点が、全体の合計点のうち上位K人に入っているかどうかを判定する
    for i in range(N):
        if sum(P[i]) >= total[-K]:
            print("Yes")
        else:
            print("No")
