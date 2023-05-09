def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # 1曲の長さの合計
    sum_a = sum(A)
    # 何周したか
    cnt = T // sum_a
    # 余り
    amari = T - cnt * sum_a
    # 余りを引いたときの曲の番号
    for i in range(N):
        amari -= A[i]
        if amari < 0:
            print(i+1, A[i]+amari)
            break

if __name__ == '__main__':
    main()