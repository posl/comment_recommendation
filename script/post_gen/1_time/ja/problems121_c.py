Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    AB = list(zip(A, B))
    AB.sort()

    ans = 0
    for i in range(N):
        if M <= 0:
            break
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            M = 0
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]

    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 金額が安い順にソート
    A, B = zip(*sorted(zip(A, B)))

    # 金額が安い順に買い集める
    ans = 0
    for i in range(N):
        if M <= B[i]:
            ans += M * A[i]
            break
        else:
            M -= B[i]
            ans += B[i] * A[i]

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 価格の安い順にソート
    A, B = zip(*sorted(zip(A, B)))
    # 累積和
    B = [0] + list(B)
    for i in range(1, N + 1):
        B[i] += B[i - 1]
    # 価格の安い順に買っていく
    ans = 0
    for i in range(N):
        if B[i] >= M:
            ans += A[i] * (M - B[i - 1])
            break
        else:
            ans += A[i] * B[i]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if M > AB[i][1]:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
        else:
            ans += AB[i][0] * M
            break
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if AB[i][1] > M:
            ans += AB[i][0] * M
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    shops = []
    for _ in range(N):
        A, B = map(int, input().split())
        shops.append((A, B))
    shops.sort()
    cost = 0
    for A, B in shops:
        if M <= B:
            cost += A * M
            break
        else:
            cost += A * B
            M -= B
    print(cost)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()

    ans = 0
    for i in range(N):
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]

    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort()

    ans = 0
    for i in range(N):
        if M <= 0:
            break
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            M = 0
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(ans)

=======
Suggestion 9

def main():
    # input
    N, M = map(int, input().split())
    ABs = [[0, 0] for _ in range(N)]
    for i in range(N):
        ABs[i] = list(map(int, input().split()))

    # compute
    ABs.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if ABs[i][1] >= M:
            ans += ABs[i][0]*M
            break
        else:
            ans += ABs[i][0]*ABs[i][1]
            M -= ABs[i][1]

    # output
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())

    # A_i と B_i を格納するリスト
    A = []
    B = []

    # 入力を受け取る
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # A_i と B_i を一つのリストにまとめる
    AB = [[a, b] for a, b in zip(A, B)]

    # A_i でソートする
    AB.sort()

    # 購入する栄養ドリンクの本数
    drink = 0
    # 購入する栄養ドリンクの合計金額
    total = 0

    # 栄養ドリンクを M 本買うまでループする
    while drink < M:
        # A_i が最小の栄養ドリンクを買う
        total += AB[0][0] * AB[0][1]
        drink += AB[0][1]
        # 買った栄養ドリンクの本数を引く
        AB[0][1] = 0
        # A_i が最小の栄養ドリンクを買い切ったら、次の栄養ドリンクを買う
        if AB[0][1] == 0:
            AB.pop(0)

    # M 本買った後に、余った栄養ドリンクを買う
    total -= AB[0][0] * (drink - M)

    print(total)
