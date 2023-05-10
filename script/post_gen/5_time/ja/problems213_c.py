Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i+1
    for i in range(len(b)):
        b_dict[b[i]] = i+1
    for i in range(n):
        print(a_dict[a[i]],b_dict[b[i]])

=======
Suggestion 2

def main():
    H, W, N = map(int, input().split())
    card = []
    for i in range(N):
        A, B = map(int, input().split())
        card.append((A, B, i + 1))
    card.sort(key=lambda x: (x[0], x[1], x[2]))
    ans = [0] * N
    for i in range(N):
        ans[i] = [card[i][0], card[i][1], card[i][2]]
    for i in range(N - 1, 0, -1):
        if ans[i][0] == ans[i - 1][0]:
            ans[i][0] = ans[i - 1][0]
            ans[i][1] = ans[i - 1][1]
        else:
            ans[i][0] = ans[i - 1][0]
            ans[i][1] = ans[i - 1][1] + 1
    for i in range(N):
        print(ans[i][0], ans[i][1])
    return

=======
Suggestion 3

def f(H,W,N,AB):
    #print(H,W,N,AB)
    #print(AB)
    #print(AB[0][0],AB[0][1])
    #print(AB[1][0],AB[1][1])
    #print(AB[2][0],AB[2][1])
    #print(AB[3][0],AB[3][1])
    #print(AB[4][0],AB[4][1])
    #print(AB[5][0],AB[5][1])
    #print(AB[6][0],AB[6][1])
    #print(AB[7][0],AB[7][1])
    #print(AB[8][0],AB[8][1])
    #print(AB[9][0],AB[9][1])
    #print(AB[10][0],AB[10][1])
    #print(AB[11][0],AB[11][1])
    #print(AB[12][0],AB[12][1])
    #print(AB[13][0],AB[13][1])
    #print(AB[14][0],AB[14][1])
    #print(AB[15][0],AB[15][1])
    #print(AB[16][0],AB[16][1])
    #print(AB[17][0],AB[17][1])
    #print(AB[18][0],AB[18][1])
    #print(AB[19][0],AB[19][1])
    #print(AB[20][0],AB[20][1])
    #print(AB[21][0],AB[21][1])
    #print(AB[22][0],AB[22][1])
    #print(AB[23][0],AB[23][1])
    #print(AB[24][0],AB[24][1])
    #print(AB[25][0],AB[25][1])
    #print(AB[26][0],AB[26][1])
    #print(AB[27][0],AB[27][1])
    #print(AB[28][0],AB[28][1])
    #print(AB[29][0],AB[29][

=======
Suggestion 4

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = [[0 for j in range(2)] for i in range(N)]
    for i in range(N):
        ans[i][0] = A[i]
        ans[i][1] = B[i]

    ans.sort(key=lambda x: x[0] + x[1])

    for i in range(N):
        print(ans[i][0], ans[i][1])

=======
Suggestion 5

def main():
    # 標準入力受付
    h, w, n = map(int, input().split())
    cards = []
    for i in range(n):
        a, b = map(int, input().split())
        cards.append((a, b, i + 1))

    # 行の削除
    cards.sort(key=lambda x: x[0])
    row = 1
    for i in range(n):
        if row != cards[i][0]:
            row = cards[i][0]
        cards[i] = (row, cards[i][1], cards[i][2])

    # 列の削除
    cards.sort(key=lambda x: x[1])
    col = 1
    for i in range(n):
        if col != cards[i][1]:
            col = cards[i][1]
        cards[i] = (cards[i][0], col, cards[i][2])

    # 答えの出力
    cards.sort(key=lambda x: x[2])
    for i in range(n):
        print(cards[i][0], cards[i][1])

=======
Suggestion 6

def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0])
    AB = sorted(AB, key=lambda x: x[1])
    print(AB)
    for i in range(N):
        print(AB[i][0], AB[i][1])

=======
Suggestion 7

def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A_sorted = sorted(A)
    B_sorted = sorted(B)
    A_dict = {}
    B_dict = {}
    for i in range(N):
        A_dict[A_sorted[i]] = i+1
        B_dict[B_sorted[i]] = i+1
    for i in range(N):
        print(A_dict[A[i]], B_dict[B[i]])

=======
Suggestion 8

def main():
    H,W,N = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)

    #Aの最小値とBの最小値を求める
    minA = min(A)
    minB = min(B)
    #print(minA)
    #print(minB)

    #AとBをそれぞれminAとminBから引く
    for i in range(N):
        A[i] -= minA
        B[i] -= minB
    #print(A)
    #print(B)

    #AとBの最大値を求める
    maxA = max(A)
    maxB = max(B)
    #print(maxA)
    #print(maxB)

    #AとBをそれぞれmaxAとmaxBから引く
    for i in range(N):
        A[i] -= maxA
        B[i] -= maxB
    #print(A)
    #print(B)

    #AとBの最大値+1を求める
    maxA = max(A)+1
    maxB = max(B)+1
    #print(maxA)
    #print(maxB)

    #AとBの最大値+1をそれぞれ足す
    for i in range(N):
        A[i] += maxA
        B[i] += maxB
    #print(A)
    #print(B)

    #AとBをそれぞれminAとminBに足す
    for i in range(N):
        A[i] += minA
        B[i] += minB
    #print(A)
    #print(B)

    #AとBをそれぞれ1ずつ足す
    for i in range(N):
        A[i] += 1
        B[i] += 1
    #print(A)
    #print(B)

    #AとBの最大値を求める
    maxA = max(A)
    maxB = max(B)
    #print(maxA)
    #print(maxB)

    #カードの

=======
Suggestion 9

def main():
    h,w,n = map(int,input().split())
    d = {}
    for i in range(n):
        a,b = map(int,input().split())
        d[(a,b)] = i+1
    a = []
    for i in range(1,h+1):
        a.append([d[(i,j)] for j in range(1,w+1) if (i,j) in d])
    b = []
    for i in range(1,w+1):
        b.append([d[(j,i)] for j in range(1,h+1) if (j,i) in d])
    for i in range(h):
        if len(a[i]) == 0:
            a[i] = [0]
    for i in range(w):
        if len(b[i]) == 0:
            b[i] = [0]
    for i in range(h):
        print(" ".join(map(str,a[i])))
    for i in range(w):
        print(" ".join(map(str,b[i])))

=======
Suggestion 10

def main():
    h,w,n = map(int,input().split())
    card = {}
    for i in range(1,n+1):
        a,b = map(int,input().split())
        card[i] = [a,b]

    #print(card)

    rows = {}
    cols = {}

    for i in range(1,h+1):
        rows[i] = 0

    for i in range(1,w+1):
        cols[i] = 0

    for i in range(1,n+1):
        rows[card[i][0]] += 1
        cols[card[i][1]] += 1

    #print(rows)
    #print(cols)

    #print(sorted(rows.items(), key=lambda x:x[1]))
    #print(sorted(cols.items(), key=lambda x:x[1]))

    for i in range(1,h+1):
        if rows[i] == 0:
            del rows[i]

    for i in range(1,w+1):
        if cols[i] == 0:
            del cols[i]

    #print(rows)
    #print(cols)

    rows = sorted(rows.items(), key=lambda x:x[1])
    cols = sorted(cols.items(), key=lambda x:x[1])

    #print(rows)
    #print(cols)

    #print(rows[0][0])
    #print(cols[0][0])

    #print(rows[0][1])
    #print(cols[0][1])

    for i in range(1,n+1):
        if rows[0][1] < cols[0][1]:
            print(rows[0][0],card[i][1])
            rows[0] = (rows[0][0],rows[0][1]+1)
        else:
            print(card[i][0],cols[0][0])
            cols[0] = (cols[0][0],cols[0][1]+1)
