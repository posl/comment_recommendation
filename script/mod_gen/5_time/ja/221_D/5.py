def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N)
    #print(A)
    #print(B)
    # 1. 各プレイヤーがログインしていた日付を全て配列に入れる
    # 2. 日付をソートする
    # 3. 各日付について、その日付が何人ログインしていたかを数える
    # 4. 出力
    # 1. 各プレイヤーがログインしていた日付を全て配列に入れる
    dates = []
    for i in range(N):
        for j in range(B[i]):
            dates.append(A[i] + j)
    #print(dates)
    # 2. 日付をソートする
    dates.sort()
    #print(dates)
    # 3. 各日付について、その日付が何人ログインしていたかを数える
    #    その日付が何人ログインしていたかを数えるには、
    #    その日付より前にログインしていた人数を数える必要がある。
    #    そのため、日付ごとに、その日付より前にログインしていた人数を記録する配列を作る。
    #    その配列を作りながら、その日付が何人ログインしていたかを数える。
    #    その日付より前にログインしていた人数を記録する配列の初期値は0とする。
    #    その日付が何人ログインしていたかを数えるには、
    #    その日付が出現した回数を数える必要がある。
    #    そのため、日付ごとに、その日付が出現した回数を記録する配列を

if __name__ == '__main__':
    solve()