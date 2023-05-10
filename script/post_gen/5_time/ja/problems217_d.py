Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
            cut.sort()
        else:
            left = 0
            right = len(cut) - 1
            while right - left > 1:
                mid = (left + right) // 2
                if cut[mid] > x:
                    right = mid
                else:
                    left = mid
            print(cut[right] - cut[left])

=======
Suggestion 2

def main():
    L,Q = map(int,input().split())
    cut = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for j in range(1,len(cut)):
                if cut[j-1] < x and x < cut[j]:
                    print(cut[j] - cut[j-1])
                    break

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    query = []
    for _ in range(Q):
        c, x = map(int, input().split())
        query.append((c, x))
    query.reverse()
    ans = []
    ans.append(L)
    for c, x in query:
        if c == 1:
            ans.append(min(x, ans[-1] - x))
        else:
            ans.append(min(x, ans[-1]))
    ans.reverse()
    for i in range(1, Q + 1):
        print(ans[i])

=======
Suggestion 4

def main():
    L,Q = map(int,input().split())
    X = [0,L]
    C = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            idx = X.index(x)
            C.append(X[idx+1] - X[idx-1])
    C.sort()
    for i in range(1,Q+1):
        print(C[i])

=======
Suggestion 5

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            idx = cut.index(x)
            print(cut[idx] - cut[idx - 1])
    return

=======
Suggestion 6

def main():
    # L:木材の長さ
    # Q:クエリの数
    L, Q = map(int, input().split())
    # 木材の長さを保存する配列
    wood = [L]
    # クエリを保存する配列
    query = []
    # クエリの数だけループ
    for i in range(Q):
        # クエリを保存
        query.append(list(map(int, input().split())))
    # クエリを処理
    for i in range(Q):
        # クエリが1の場合
        if query[i][0] == 1:
            # 木材を分割
            wood = wood_division(wood, query[i][1])
        # クエリが2の場合
        elif query[i][0] == 2:
            # 木材の長さを出力
            print(wood_length(wood, query[i][1]))

=======
Suggestion 7

def main():
    L, Q = map(int, input().split())
    X = [0] * (Q + 1)
    for i in range(1, Q + 1):
        c, x = map(int, input().split())
        X[i] = x
    X.sort()
    #print(X)
    #print(L)
    #print(Q)
    #print(X)
    #print(X[1])
    #print(X[2])
    #print(X[3])
    #print(X[4])
    #print(X[5])
    #print(X[6])
    #print(X[7])
    #print(X[8])
    #print(X[9])
    #print(X[10])
    #print(X[11])
    #print(X[12])
    #print(X[13])
    #print(X[14])
    #print(X[15])
    #print(X[16])
    #print(X[17])
    #print(X[18])
    #print(X[19])
    #print(X[20])
    #print(X[21])
    #print(X[22])
    #print(X[23])
    #print(X[24])
    #print(X[25])
    #print(X[26])
    #print(X[27])
    #print(X[28])
    #print(X[29])
    #print(X[30])
    #print(X[31])
    #print(X[32])
    #print(X[33])
    #print(X[34])
    #print(X[35])
    #print(X[36])
    #print(X[37])
    #print(X[38])
    #print(X[39])
    #print(X[40])
    #print(X[41])
    #print(X[42])
    #print(X[43])
    #print(X[44])
    #print(X[45])
    #print(X[46])
    #print(X[47])
    #print(X[48])
    #print(X[49])
    #print(X[50])
    #print(X[51])
    #print(X[52])
    #print(X[53])
    #print(X[54])
    #print(X[55])
    #print(X[56])
    #print(X[57])
    #print(X[58])
    #print(X[59])
    #print(X

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.buffer.readline
    L,Q = map(int,readline().split())
    X = [0,L]
    for _ in range(Q):
        c,x = map(int,readline().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            idx = X.index(x)
            print(X[idx+1]-X[idx-1])

=======
Suggestion 9

def main():
    L, Q = map(int, input().split())
    X = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            idx = X.index(x)
            print(X[idx] - X[idx - 1])

=======
Suggestion 10

def main():
    L, Q = map(int, input().split())
    q = [list(map(int, input().split())) for _ in range(Q)]
    q = [[c, x] for c, x in q if c == 1]
    q.sort(key=lambda x: x[1])
    ans = [0] * Q
    ans[0] = L
    for i in range(1, len(q)):
        ans[i] = q[i][1] - q[i - 1][1]
    ans[-1] = L - q[-1][1]
    for i in range(Q):
        if q[i][0] == 2:
            print(ans[i])
