def solve():
    # 整数 1 つ
    #n = int(input())
    # 整数複数個
    h, w = map(int, input().split())
    # スペース区切り整数複数個
    #a, b = map(int, input().split())
    # 文字列 1 つ
    #s = input()
    # 文字列複数個
    #s = input().split()
    # 整数リスト
    #a = list(map(int, input().split()))
    # 整数リスト複数行
    #a = [int(input()) for _ in range(n)]
    # 整数リスト複数行複数列
    #a = [list(map(int, input().split())) for _ in range(n)]
    # 文字列リスト複数行
    #s = [input() for _ in range(n)]
    a = [list(map(int, input().split())) for _ in range(h)]
    min_a = 101
    for i in range(h):
        for j in range(w):
            min_a = min(min_a, a[i][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_a
    print(ans)
