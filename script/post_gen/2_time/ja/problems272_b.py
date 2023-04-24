Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(M):
            if i != j:
                for k in range(1, len(a[i])):
                    for l in range(1, len(a[j])):
                        if a[i][k] == a[j][l]:
                            print("Yes")
                            return
    print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * N
    for _ in range(M):
        B = list(map(int, input().split()))
        for b in B[1:]:
            A[b-1] += 1
    print('Yes' if max(A) > 1 else 'No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    all = set()
    for i in range(M):
        k = list(map(int, input().split()))
        k.pop(0)
        all.update(k)
    if len(all) == N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    #print(N, M)
    X = [[0] * N for _ in range(N)] # 2次元配列の初期化
    for i in range(M):
        k = list(map(int, input().split()))
        #print(k)
        for j in range(1, k[0]+1):
            for l in range(j+1, k[0]+1):
                X[k[j]-1][k[l]-1] = 1
                X[k[l]-1][k[j]-1] = 1
    #print(X)
    for i in range(N):
        for j in range(N):
            if X[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print()

    #舞踏会に参加した人のリスト
    dance = []
    for i in range(M):
        #print(i)
        k_i = int(input())
        #print(k_i)
        x = list(map(int, input().split()))
        #print(x)
        dance.append(x)
        #print(dance)
        #print()

    #print(dance)

    #舞踏会に参加した人のリストを集合に変換
    #print()
    dance_set = []
    for i in range(M):
        #print(i)
        x = set(dance[i])
        #print(x)
        dance_set.append(x)
        #print(dance_set)
        #print()

    #print(dance_set)

    #舞踏会に参加した人のリストを集合に変換
    #print()
    dance_set = []
    for i in range(M):
        #print(i)
        x = set(dance[i])
        #print(x)
        dance_set.append(x)
        #print(dance_set)
        #print()

    #print(dance_set)

    #舞踏会に参加した人のリストを集合に変換
    #print()
    dance_set = []
    for i in range(M):
        #print(i)
        x = set(dance[i])
        #print(x)
        dance_set.append(x)
        #print(dance_set)
        #print()

    #print(dance_set)

    #舞踏会に参加した人のリストを集合に変換
    #print()
    dance_set = []
    for i in range(M):
        #print(i)
        x = set(dance[i])
        #print(x)
        dance_set.append(x)
        #print(dance_set)
        #print()

    #print(dance_set)

    #舞踏会に参加した人のリストを集合に変換
    #print()
    dance_set = []
    for i in range(M):
        #print(i)
        x = set(dance[i])
        #print(x)

=======
Suggestion 6

def main():
    N, M = list(map(int, input().split()))
    #N人の人が、M回の舞踏会に参加したかどうかを記録する
    #人は1からNまでの番号がついている
    #参加した場合は1、参加していない場合は0
    people = [[0] * M for i in range(N)]
    for i in range(M):
        a = list(map(int, input().split()))
        for j in range(a[0]):
            people[a[j+1]-1][i] = 1

    #print(people)
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            for k in range(M):
                if people[i][k] == 1 and people[j][k] == 1:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print()
    #print("入力例 1の場合")
    #N=3
    #M=3
    #print(N, M)
    #print()
    #print("入力例 2の場合")
    #N=4
    #M=2
    #print(N, M)
    #print()
    #print("入力例 3の場合")
    #N=5
    #M=5
    #print(N, M)
    #print()
    #print("入力例 4の場合")
    #N=8
    #M=5
    #print(N, M)
    #print()
    #print("入力例 5の場合")
    #N=10
    #M=10
    #print(N, M)
    #print()
    #print("入力例 6の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 7の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 8の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 9の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 10の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 11の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 12の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例 13の場合")
    #N=100
    #M=100
    #print(N, M)
    #print()
    #print("入力例

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    #print(N,M)
    #print("")

    #舞踏会の参加者をリストに格納
    list = []
    for i in range(M):
        l = list(map(int,input().split()))
        list.append(l)
    #print(list)
    #print("")

    #参加者のリストを集合に変換
    set_list = []
    for i in range(M):
        s = set(list[i])
        set_list.append(s)
    #print(set_list)
    #print("")

    #集合の積を求める
    s = set_list[0]
    for i in range(1,M):
        s = s & set_list[i]
    #print(s)

    if len(s) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 人数N, 舞踏会数M
    # print(N, M)
    # 人数分のリストを作成
    # 0は未参加、1は1回以上参加
    people = [0] * N
    # print(people)
    for i in range(M):
        # 舞踏会の出席者数
        K = int(input())
        # print(K)
        # 舞踏会に出席した人のリスト
        attend = list(map(int, input().split()))
        # print(attend)
        for j in range(K):
            # print(attend[j])
            # 出席者が1人でもいれば1
            people[attend[j] - 1] = 1
    # print(people)
    for i in range(N):
        if people[i] == 0:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #人数と舞踏会の回数を受け取る
    #print(N,M)
    #print("----------")

    #舞踏会の回数分ループ
    for i in range(M):
        #参加者の人数と参加者の番号を受け取る
        k, *x = map(int, input().split())
        #print(k,x)

        #参加者の人数分ループ
        for j in range(k):
            #参加者の番号を受け取る
            x[j] = int(x[j])
            #print(x[j],end=" ")
        #print()

        #参加者の人数分ループ
        for j in range(k):
            #参加者の番号を受け取る
            x[j] = int(x[j])
            #print(x[j],end=" ")
        #print()

    #舞踏会の回数分ループ
    for i in range(M):
        #参加者の人数と参加者の番号を受け取る
        k, *x = map(int, input().split())
        #print(k,x)

        #参加者の人数分ループ
        for j in range(k):
            #参加者の番号を受け取る
            x[j] = int(x[j])
            #print(x[j],end=" ")
        #print()

        #参加者の人数分ループ
        for j in range(k):
            #参加者の番号を受け取る
            x[j] = int(x[j])
            #print(x[j],end=" ")
        #print()

    #舞踏会の回数分ループ
    for i in range(M):
        #参加者の人数と参加者の番号を受け取る
        k, *x = map(int, input().split())
        #print(k,x)

        #参加者の人数分ループ
        for j in range(k):
            #参加者の番号を受け取
