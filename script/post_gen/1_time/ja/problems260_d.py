Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    for i in range(N):
        P[i] -= 1
    stack = [0] * N
    stack[0] = 0
    top = 0
    for i in range(N):
        if P[i] > stack[top]:
            top += 1
            stack[top] = P[i]
        else:
            while top >= 0 and stack[top] >= P[i]:
                ans[stack[top]] = i + 1
                top -= 1
            top += 1
            stack[top] = P[i]
    for i in range(N):
        if ans[i] == -1:
            ans[i] = N + K
    print(*ans, sep='
')

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        p[i] -= 1
    for i in range(n):
        if ans[i] != -1:
            continue
        now = i
        for j in range(k):
            if ans[now] != -1:
                break
            ans[now] = i + 1
            now = p[now]
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # 1 から N が書かれた N 枚のカードが裏向きで積まれた山札があり、上から i 枚目のカードには整数 P_i が書かれています。
    # この山札を使って、以下の行動を N ターン繰り返します。
    # 山札の一番上のカードを引いて、そこに書かれた整数を X とする。
    # 場に見えている表向きのカードであって書かれた整数が X 以上であるもののうち、書かれた整数が最小のものの上に、引いたカードを表向きで重ねる。もし場にそのようなカードがなければ、引いたカードをどれにも重ねずに表向きで場に置く。
    # その後、表向きのカードが K 枚重ねられた山が場にあればその山のカードを全て食べる。食べられたカードは全て場から消滅する。
    # 各カードについて、何ターン目に食べられるか、あるいは最後まで食べられないかを求めてください。
    # 制約
    # 入力は全て整数
    # 1 ≦ K ≦ N ≦ 2 × 10^5
    # P は (1,2,...,N) の順列 ( (1,2,...,N) を並べ替えて得られる列 ) である
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # N K
    # P_1 P_

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [i - 1 for i in P]
    #print(N, K)
    #print(P)
    #食べられたカードのリスト
    eat = []
    #食べられたカードの番号と食べられたターンを対応させた辞書
    eat_turn = {}
    #食べられたカードの番号を格納するリスト
    eat_num = []
    #食べられたカードの番号と食べられたターンを対応させた辞書
    eat_turn = {}
    #食べられたカードの番号を格納するリスト
    eat_num = []
    #食べられたカードの番号と食べられたターンを対応させた辞書
    eat_turn = {}
    #食べられたカードの番号を格納するリスト
    eat_num = []
    #食べられたカードの番号と食

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [i-1 for i in P]
    ans = [-1]*N
    card = [-1]*N
    for i in range(N):
        card[P[i]] = i
    for i in range(N):
        if ans[i] != -1:
            continue
        ans[i] = i+1
        j = i
        while card[j] >= K-1:
            ans[j] = i+1
            j = card[j] - K + 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # そのカードが食べられるターン
    ans = [-1] * N
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []

    # そのカードが食べられるターン
    ans = [-1] * N
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるターンを記録する
    eat = []

    # そのカードが食べられるターン
    ans = [-1] * N
    # そのカードが食べられるターンを記録する
    eat = []
    # そのカードが食べられるター

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    PQ = [(-1, -1) for _ in range(N + 1)]
    for i in range(N):
        PQ[P[i]] = (i, -1)
    for i in range(N):
        PQ[P[i]] = (PQ[P[i]][0], i)
    PQ = PQ[1:]
    PQ.sort(key=lambda x: x[0])
    ans = [-1 for _ in range(N)]
    for i in range(N):
        if PQ[i][1] - PQ[i][0] >= K - 1:
            ans[PQ[i][1]] = PQ[i][1] + 1
    for i in range(N):
        if ans[i] == -1:
            continue
        for j in range(i + 1, N):
            if ans[j] == -1:
                if PQ[j][1] - PQ[i][1] >= K:
                    ans[j] = ans[i]
                else:
                    break
            else:
                break
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # 1-indexed
    P = [0] + P

    # 1-indexed
    eaten = [-1] * (N + 1)
    # 1-indexed
    stack = [0] * (N + 1)
    # 1-indexed
    stack_index = [0] * (N + 1)

    for i in range(1, N + 1):
        # stack に stack_index が K 以上のカードがない場合、
        # P[i] を stack に積む
        if stack_index[K] == 0:
            stack_index[P[i]] += 1
            stack[stack_index[P[i]]] = P[i]
        else:
            # stack に stack_index が K 以上のカードがある場合、
            # P[i] が stack_index 以上のカードのうち、最小のカードの上に積む
            # その後、stack_index 以上のカードを食べる
            # これにより、stack_index が K になる
            stack_index[P[i]] = stack_index[K] + 1
            stack[stack_index[P[i]]] = P[i]

            # stack_index 以上のカードを食べる
            for j in range(stack_index[K], 0, -1):
                eaten[stack[j]] = i
                stack_index[stack[j]] = 0

            # stack_index が K になる
            stack_index[K] = K

    for i in range(1, N + 1):
        print(eaten[i])

=======
Suggestion 9

def main():
    #入力
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    #カードが重なっているかを判定するリスト
    #重なっているカードの枚数がK枚に達したら、そのカードを食べる
    #食べたカードは-1にする
    #重なっているカードの枚数がK枚に達したかを判定する
    #重なっているカードの枚数がK枚に達したら、そのカードを食べる
    #食べたカードは-1にする
    #食べられたカード数をカウントする
    #食べられたカード数がN枚に達したら終了
    #食べられたカード数がN枚に達していないなら、食べられなかったカードを出力

    #カードが重なっているかを判定するリスト
    #重なっているカードの枚数がK枚に達したら、そのカードを食べる
    #食べたカードは-1にする
    #重なっているカードの枚数がK枚に達したかを判定する
    #重なっているカードの枚数がK枚に達したら、そのカードを食べる
    #食べたカードは-1にする
    #食べられたカード数をカウントする
    #食べられたカード数がN枚に達したら終了
    #食べられたカード数がN枚に達していないなら、食べられなかったカードを出力

    #カードが重なっているかを判

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # print(N, K)
    # print(P)

    # 1からNの配列を作成
    cards = [i for i in range(1, N+1)]
    print(cards)
    # 1からNの配列をPの順番に並び替え
    cards = [cards[i-1] for i in P]
    print(cards)
    # 1からNの配列をPの順番に並び替え
    cards = [cards[i-1] for i in P]
    print(cards)
