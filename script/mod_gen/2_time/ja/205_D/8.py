def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    for i in range(Q):
        # リストの中にK[i]があればそのインデックスを返す
        if K[i] in A:
            print(K[i])
            continue
        # リストの中にK[i]がなければ、K[i]より大きい数の中で最小の数を返す
        # なければ、リストの中で最大の数を返す
        else:
            print(min([a for a in A if a > K[i]], default=max(A)))

if __name__ == '__main__':
    main()