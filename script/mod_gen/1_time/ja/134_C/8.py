def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    # Aの中で最大値を求める
    maxA = max(A)
    # Aの中で最大値を2つ以上持つ要素があるかどうか
    maxA_cnt = A.count(maxA)
    # Aの中で最大値を2つ以上持つ要素がある
    if maxA_cnt > 1:
        for i in range(N):
            print(maxA)
    # Aの中で最大値を2つ以上持つ要素がない
    else:
        # Aの中で最大値を持つ要素のindexを求める
        maxA_idx = A.index(maxA)
        # Aの中で最大値を持つ要素以外の最大値を求める
        maxA2 = max(A[:maxA_idx] + A[maxA_idx+1:])
        for i in range(N):
            if i == maxA_idx:
                print(maxA2)
            else:
                print(maxA)

if __name__ == '__main__':
    main()