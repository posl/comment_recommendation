Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for i in range(len(cut)):
                if cut[i] == x:
                    print(cut[i + 1] - cut[i - 1])
                    break

=======
Suggestion 2

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            print(cut[cut.index(x) + 1] - cut[cut.index(x) - 1])

=======
Suggestion 3

def main():
    l, q = map(int, input().split())
    cut = [0, l]
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for j in range(len(cut)):
                if cut[j] == x:
                    print(cut[j+1] - cut[j-1])
                    cut.pop(j)
                    break

=======
Suggestion 4

def main():
    L,Q = map(int,input().split())
    tree = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            tree.append(x)
        else:
            tree.sort()
            left = tree.index(x)
            print(tree[left]-tree[left-1])

=======
Suggestion 5

def main():
    l, q = map(int, input().split())
    cut = [0] * (q + 1)
    for i in range(1, q + 1):
        c, x = map(int, input().split())
        if c == 1:
            cut[i] = x
    cut = sorted(cut)
    cut.append(l)
    for i in range(1, q + 1):
        cut[i] += cut[i - 1]
    for i in range(1, q + 1):
        print(cut[i] - cut[i - 1])

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    q_list = []
    for i in range(Q):
        c, x = map(int, input().split())
        q_list.append((c, x))
    #print(q_list)
    #print(L, Q)
    #print(q_list[0][0])

    #木材の長さを管理する配列
    woods = [L]
    #print(woods)
    #クエリの回数分繰り返す
    for i in range(Q):
        #print("i:", i)
        #print("woods:", woods)
        #print("q_list:", q_list[i])
        #クエリが1の場合
        if q_list[i][0] == 1:
            #print("q_list[i][1]:", q_list[i][1])
            #print("woods.index(q_list[i][1]):", woods.index(q_list[i][1]))
            #print("woods[woods.index(q_list[i][1])]:", woods[woods.index(q_list[i][1])])
            #print("woods[woods.index(q_list[i][1])] - q_list[i][1]:", woods[woods.index(q_list[i][1])] - q_list[i][1])
            #print("q_list[i][1] - woods[woods.index(q_list[i][1]) - 1]:", q_list[i][1] - woods[woods.index(q_list[i][1]) - 1])
            #print("woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1]:", woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1])
            #print("woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1] - 1:", woods[woods.index(q_list[i][1])] - q_list[i][1] + q_list[i][1] - woods[woods.index(q_list[i][1]) - 1] - 1)
            #print("woods

=======
Suggestion 7

def main():
    L, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        c, x = map(int, input().split())
        queries.append((c, x))
    print(queries)

=======
Suggestion 8

def main():
    # L, Q = map(int, input().split())
    L = 100
    Q = 10
    # c_x = [list(map(int, input().split())) for _ in range(Q)]
    c_x = [[1, 31], [2, 41], [1, 59], [2, 26], [1, 53], [2, 58], [1, 97], [2, 93], [1, 23], [2, 84]]

    # 木材の長さ
    wood_len = [L]

    # クエリの回数
    query_num = 0

    # クエリの処理
    for c, x in c_x:
        if c == 1:
            # 木材の長さを更新
            idx = -1
            for i in range(len(wood_len)):
                if wood_len[i] > x:
                    idx = i
                    break
            if idx == -1:
                wood_len.append(x)
            else:
                wood_len[idx] -= x
                wood_len.insert(idx, x)

        else:
            # クエリの回数を更新
            query_num += 1

            # 木材の長さを出力
            print(wood_len[x-1])

    # クエリの回数を出力
    print(query_num)

=======
Suggestion 9

def main():
    L,Q = map(int,input().split())
    cut_list = []
    for i in range(Q):
        cut_list.append(list(map(int,input().split())))
    cut_list.reverse()
    cut_list.append([0,0])
    cut_list.reverse()
    cut_list.append([0,L])
    cut_list.reverse()
    cut_list.append([0,L])
    cut_list.reverse()
    cut_list.append([0,0])
    cut_list.reverse()
    cut_list.append([0,0])
    cut_list.reverse()
    cut_list.append([0,L])
    cut_list.reverse()
    cut_list.append([0,L])

    #print(cut_list)

    cut_num = 0
    cut_left = 0
    cut_right = L
    for i in range(1,Q+1):
        if cut_list[i][0] == 1:
            if cut_list[i][1] < cut_left:
                cut_num += 0
            elif cut_list[i][1] > cut_right:
                cut_num += 0
            else:
                cut_num += 1
                cut_right = cut_list[i][1]
                cut_left = cut_list[i][1]
        elif cut_list[i][0] == 2:
            print(cut_right-cut_left)
        else:
            print("error")
        #print(cut_num,cut_left,cut_right)

=======
Suggestion 10

def main():
    L,Q = map(int,input().split())
    #print(L,Q)
    #prin
