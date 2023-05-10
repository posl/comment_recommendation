def solve():
    # 整数 1 つ
    #N = int(input())
    # 整数複数個
    #A, B = map(int, input().split())
    # 整数複数個（リスト）
    #A = list(map(int, input().split()))
    # 文字列 1 つ
    #S = input()
    # 文字列複数個
    #S = [input() for i in range(N)]
    # 整数 N 個
    #A = [int(input()) for i in range(N)]
    # 整数 N 個（スペース区切り一括入力）
    #A = list(map(int, input().split()))
    # 整数 N 個（改行区切り一括入力）
    #A = [int(input()) for i in range(N)]
    S = [input() for i in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                cnt += 1
    print(cnt)
