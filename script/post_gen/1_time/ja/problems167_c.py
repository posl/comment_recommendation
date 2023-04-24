Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        a = [0]*M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    a[k] += A[j][k]
        if all(x >= X for x in a):
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 2

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    ans = 10**9
    for i in range(2**N):
        tmp = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]

        if all([x >= X for x in tmp]):
            ans = min(ans, cost)

    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for n in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    min_cost = 1000000000
    for i in range(2**N):
        cost = 0
        a = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    a[k] += A[j][k]
        if all(x >= X for x in a):
            min_cost = min(min_cost, cost)

    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())

    ans = 10**10
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if all(u >= X for u in understanding):
            ans = min(ans, cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def main():
    #入力
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    
    #全探索
    ans = 10**9
    for i in range(2**N):
        #理解度の合計
        sum_a = [0]*M
        #合計金額
        sum_c = 0
        for j in range(N):
            if i >> j & 1:
                sum_c += C[j]
                for k in range(M):
                    sum_a[k] += A[j][k]
        #理解度がX以上か
        if all(a >= X for a in sum_a):
            ans = min(ans, sum_c)
    
    #出力
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 6

def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = float("inf")
    for i in range(2**N):
        total = 0
        score = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                total += A[j][0]
                for k in range(M):
                    score[k] += A[j][k+1]
        if all(s >= X for s in score):
            ans = min(ans, total)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**6
    for i in range(2**N):
        B = [0]*M
        C = 0
        for j in range(N):
            if (i>>j)&1:
                C += A[j][0]
                for k in range(M):
                    B[k] += A[j][k+1]
        if all(x>=X for x in B):
            ans = min(ans, C)
    if ans == 10**6:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def main():
    N, M, X = map(int, input().split())
    book = [list(map(int, input().split())) for i in range(N)]
    ans = 10 ** 9 + 1
    for i in range(2 ** N):
        cost = 0
        ability = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += book[j][0]
                for k in range(M):
                    ability[k] += book[j][k + 1]
        if min(ability) >= X:
            ans = min(ans, cost)
    if ans == 10 ** 9 + 1:
        print(-1)
    else:
        print(ans)

=======
Suggestion 9

def main():
    # N: 参考書の種類数
    # M: アルゴリズムの種類数
    # X: 目標
    N, M, X = map(int, input().split())
    # C: 参考書の値段
    # A: アルゴリズムの理解度
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])

    # 組み合わせ全探索
    # bit全探索で、参考書を買うか買わないかを全探索
    # それぞれの組み合わせで、アルゴリズムの理解度を計算
    # その中で、X以上のものがあれば、最小値を出力
    # なければ、-1を出力
    ans = 10 ** 10
    for i in range(2 ** N):
        # 2進数に変換
        s = format(i, "b").zfill(N)
        # アルゴリズムの理解度を計算
        # それぞれのアルゴリズムの理解度を0に初期化
        tmp = [0] * M
        # 金額の合計
        money = 0
        for j in range(N):
            if s[j] == "1":
                money += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        # 一つでも理解度がX未満ならば、次のループへ
        if min(tmp) < X:
            continue
        # それ以外ならば、金額の合計を更新
        ans = min(ans, money)
    # -1を出力
    if ans == 10 ** 10:
        print(-1)
    # 最小値を出力
    else:
        print(ans
