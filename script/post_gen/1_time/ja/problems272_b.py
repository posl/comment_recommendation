Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [set() for i in range(M)]
    for i in range(M):
        k, *x = map(int, input().split())
        for j in range(k):
            A[i].add(x[j])

    for i in range(M):
        for j in range(i+1, M):
            if A[i] & A[j]:
                print("Yes")
                return

    print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    people = [0] * N
    for i in range(M):
        k, *x = map(int, input().split())
        for j in range(k):
            people[x[j] - 1] += 1
    for i in range(N):
        if people[i] == 0:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    a = [0]*n
    for i in range(m):
        b = list(map(int, input().split()))
        for j in range(b[0]):
            a[b[j+1]-1] += 1
    for i in range(n):
        if a[i] == 0:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    ans = "No"
    for i in range(M):
        k,*x = map(int,input().split())
        for j in range(1,k):
            if x[j-1]+1 == x[j]:
                ans = "Yes"
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    # print(N, M)
    k = []
    x = []
    for i in range(M):
        k.append(input().split())
        # print(k[i])
        x.append(k[i][1:])
        # print(x[i])
    # print(x)
    ans = "No"
    for i in range(M):
        for j in range(i+1, M):
            if len(set(x[i]) & set(x[j])) > 0:
                ans = "Yes"
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    # 0 で初期化した N×N の行列を作成
    # 0 は参加していないことを示す
    # 1 は参加していることを示す
    # 今回は 0 と 1 だけを使うので、bool ではなく int を使っても良い
    # 2 は人 i と人 j が共に参加していることを示す
    # これは最後に出力する際に使う
    # 0 と 1 は入力の際に使う
    # 2 は出力の際に使う
    table = [[0 for i in range(N)] for j in range(N)]
    
    for i in range(M):
        # 1 回目の舞踏会の参加者数
        k = int(input())
        # 1 回目の舞踏会の参加者の番号
        x = list(map(int, input().split()))
        for j in range(k):
            for l in range(j+1, k):
                # 参加している人同士に 2 を代入
                table[x[j]-1][x[l]-1] = 2
                table[x[l]-1][x[j]-1] = 2
    
    for i in range(N):
        for j in range(N):
            # 2 があれば Yes を出力
            if table[i][j] == 2:
                print("Yes")
                return
    
    # 2 がなければ No を出力
    print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # 1 人目から N 人目までの人が 1 回も参加していない状態で初期化
    # 0 は参加していないことを意味する
    people = [[0] * M for _ in range(N)]
    for i in range(M):
        # 参加人数 k_i と参加者の番号 x_{i,1} x_{i,2} ... x_{i,k_i} を取得
        k_i, *x_i = map(int, input().split())
        for j in range(k_i):
            # 参加している人の人数の配列の i 番目の要素を 1 にする
            people[x_i[j] - 1][i] = 1
    # 2 重ループでどの二人も少なくとも 1 回同じ舞踏会に参加しているか調べる
    for i in range(N - 1):
        for j in range(i + 1, N):
            # どの舞踏会にも参加していない場合は No を出力して終了
            if sum([people[i][k] & people[j][k] for k in range(M)]) == 0:
                print("No")
                return
    # どの二人も少なくとも 1 回同じ舞踏会に参加している場合は Yes を出力
    print("Yes")

main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # print(N, M)
    # print(type(N), type(M))
    # print("")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print()

    #参加した人のリスト
    people = []
    for i in range(M):
        #舞踏会の参加者
        people.append(list(map(int, input().split())))
        #print(people[i])

    #print()
    #print(people)

    #舞踏会の参加者のリストを一つのリストにまとめる
    people_list = []
    for i in range(M):
        for j in range(1, people[i][0] + 1):
            people_list.append(people[i][j])

    #print()
    #print(people_list)

    #舞踏会の参加者のリストを集合に変換
    people_set = set(people_list)

    #print()
    #print(people_set)

    #舞踏会の参加者のリストの要素数と集合の要素数が同じなら
    #どの二人も少なくとも 1 回同じ舞踏会に参加した
    if len(people_list) == len(people_set):
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("-----")
    #print("-----")
    
    #参加者のリスト
    attend_list = []
    
    for i in range(M):
        #参加者の数
        k = int(input())
        #print(k)
        #参加者の番号
        x = list(map(int, input().split()))
        #print(x)
        #print("-----")
        
        #参加者の番号をリストに追加
        attend_list.append(x)
    
    #print(attend_list)
    
    #参加者の番号を集合に変換
    attend_set = [set(i) for i in attend_list]
    #print(attend_set)
    
    #参加者の集合の積集合
    attend_set_intersect = attend_set[0]
    #print(attend_set_intersect)
    
    for i in range(1, len(attend_set)):
        attend_set_intersect = attend_set_intersect & attend_set[i]
        #print(attend_set_intersect)
    
    #print(attend_set_intersect)
    
    #参加者の集合の積集合が空集合でない場合
    if attend_set_intersect:
        print("Yes")
    else:
        print("No")
