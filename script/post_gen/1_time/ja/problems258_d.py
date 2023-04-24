Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = 0
    for i in range(N-1, -1, -1):
        if X > 0:
            if A[i] >= B[i]:
                ans += B[i]
                X -= 1
            else:
                ans += A[i]
                X -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.append(0)
    B.append(0)
    A = sorted(A)
    B = sorted(B)
    ans = 0
    for i in range(N):
        if X >= A[i] + B[i]:
            ans += A[i] + B[i]
            X -= A[i] + B[i]
        else:
            ans += X
            break
    if X > 0:
        ans += min(A[N], B[N])
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = [0] + A
    B = [0] + B
    ans = 0
    for i in range(1, N+1):
        ans += min(A[i], X) * i
        X -= min(A[i], X)
        ans += min(B[i], X) * i
        X -= min(B[i], X)
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = 0
    i = 0
    while i < N:
        if A[i] < B[N - i - 1]:
            ans += A[i]
            X -= 1
            i += 1
        else:
            ans += B[N - i - 1]
            X -= 1
        if X == 0:
            break
    if X > 0:
        ans += A[i] * X
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A[i] > B[i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[i]
            X -= 1
    for i in range(X):
        ans += B[i]
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 1. ステージのゲームプレイ時間を短い順にソートする
    # 2. ステージのゲームプレイ時間を短い順にゲームプレイする
    # 3. 2.でゲームプレイしたステージのストーリー映像の時間を足す
    # 4. 3.で足した時間がXを超えたら、ストーリー映像の時間を引いて、
    #    そのステージのゲームプレイ時間を足す
    # 5. 4.で引いた時間がXを超えたら、ストーリー映像の時間を引いて、
    #    そのステージのゲームプレイ時間を足す
    # 6. 5.で引いた時間がXを超えたら、ストーリー映像の時間を引いて、
    #    そのステージのゲームプレイ時間を足す
    # 7. 6.で引いた時間がXを超えたら、ストーリー映像の時間を引いて、
    #    そのステージのゲームプレイ時間を足す
    # 8. 7.で引いた時間がXを超えたら、ストーリー映像の時間を引いて、
    #    そのステージのゲームプレイ時間を足す
    # 9. 8.で引いた時間がXを超えたら、ストーリー映像の時間を引いて、
    #    そのステージのゲームプレイ時間を足す

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A_B = []
    for a, b in zip(A, B):
        A_B.append([a, b])
    A_B.sort()
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A_B[i][0] < A_B[i][1]:
            ans += A_B[i][0]
            X -= 1
        else:
            break
    if X == 0:
        print(ans)
        return
    for i in range(N):
        if X == 0:
            break
        ans += A_B[i][1]
        X -= 1
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        X -= 1
        if X == 0:
            break
        if A[i] > B[i]:
            ans += min(A[i] - B[i], B[i])
            X -= 1
            if X == 0:
                break

    print(ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for a, b in AB:
        ans += min(X, 1) * (a + b)
        X -= 1
    print(ans)

=======
Suggestion 10

def main():
    #入力
    N,X = map(int,input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i],B[i] = map(int,input().split())

    #処理
    #ゲームプレイ時間の総和
    total = 0
    for i in range(N):
        total += B[i]
    #クリア回数
    clear = 0
    #ゲームプレイ時間の総和がXを超えるまでループ
    while total > X:
        #ゲームプレイ時間が最長のステージを探す
        max = 0
        for i in range(N):
            if max < B[i]:
                max = B[i]
                max_index = i
        #ゲームプレイ時間が最長のステージを削除
        total -= max
        B[max_index] = 0
        clear += 1

    #出力
    print(total + clear * A[0])
