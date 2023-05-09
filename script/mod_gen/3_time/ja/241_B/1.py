def main():
    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 長さのリストを作成する
    a = [0] * (10**9 + 1)
    for i in range(N):
        a[A[i]] = 1
    # 食事計画を実行できるかどうかを調べる
    for i in range(M):
        if a[B[i]] == 0:
            print('No')
            return
    # 食事計画を実行できる場合
    print('Yes')

if __name__ == '__main__':
    main()