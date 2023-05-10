def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    # 1回戦終了後の勝者リスト
    B = []
    # 1回戦終了後の敗者リスト
    C = []
    # 2回戦終了後の勝者リスト
    D = []
    # 1回戦の結果を出す
    for i in range(0, len(A), 2):
        if A[i] > A[i+1]:
            B.append(A[i])
            C.append(A[i+1])
        else:
            B.append(A[i+1])
            C.append(A[i])
    # 2回戦の結果を出す
    for i in range(0, len(B), 2):
        if B[i] > B[i+1]:
            D.append(B[i])
        else:
            D.append(B[i+1])
    # 3回戦の結果を出す
    if D[0] > D[1]:
        print(C[0])
    else:
        print(C[1])

if __name__ == '__main__':
    main()