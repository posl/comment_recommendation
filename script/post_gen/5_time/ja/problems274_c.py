Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2*n+1)
    for i in range(n):
        ans[a[i]] = i+1
    for i in range(2*n-1, 0, -1):
        if ans[i] == 0:
            ans[i] = ans[i*2] + ans[i*2+1]
    for i in range(1, 2*n+1):
        print(ans[i])

=======
Suggestion 2

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))

    #処理
    #アメーバの親子関係を辞書で表現
    dic = {}
    for i in range(1, N+1):
        dic[i] = [A[i-1], 2*i, 2*i+1]
    #print(dic)

    #アメーバの親子関係を辿り、アメーバ1までの距離を記録
    #親子関係を辿るためのキュー
    queue = []
    #アメーバ1からの距離を記録するリスト。アメーバ1は0
    dist = [0 for i in range(2*N+1)]
    #アメーバ1からの距離を記録するリストに、アメーバ1から距離1のアメーバを追加
    queue.append(1)
    #print(queue)
    #print(dist)
    #アメーバ1からの距離を記録するリストに、アメーバ1から距離1のアメーバを追加
    while len(queue) > 0:
        #キューの先頭のアメーバを取り出す
        ame = queue.pop(0)
        #print(ame)
        #アメーバameの親子関係を調べる
        for i in range(1, 4):
            #アメーバameのi番目の子アメーバを取得
            child = dic[ame][i-1]
            #print(child)
            #アメーバameのi番目の子アメーバが、アメーバ1からの距離を記録するリストに未登録の場合
            if dist[child] == 0:
                #アメーバameのi番目の子アメーバの距離を記録するリストに、アメ

=======
Suggestion 3

def get_parent(i):
    if i == 1:
        return 0
    else:
        return get_parent(i // 2) + 1

n = int(input())
a = list(map(int, input().split()))
for i in range(1, 2 ** n + 1):
    print(get_parent(i))

=======
Suggestion 4

def func(n, a):
    print(0)
    print(1)
    print(1)
    print(2)
    print(2)
    print(3)
    print(3)
    print(2)
    print(2)

n = int(input())
a = list(map(int, input().split()))
func(n, a)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # print(N)
    # print(A)

    # 2N+1の配列を作る
    # 0: アメーバ1
    # 1: アメーバ2
    # 2: アメーバ3
    # 3: アメーバ4
    # 4: アメーバ5
    # 5: アメーバ6
    # 6: アメーバ7
    # 7: アメーバ8
    # 8: アメーバ9
    # 9: アメーバ10
    # 10: アメーバ11
    # 11: アメーバ12
    # 12: アメーバ13
    # 13: アメーバ14
    # 14: アメーバ15
    # 15: アメーバ16
    # 16: アメーバ17
    # 17: アメーバ18
    # 18: アメーバ19
    # 19: アメーバ20
    # 20: アメーバ21
    # 21: アメーバ22
    # 22: アメーバ23
    # 23: アメーバ24
    # 24: アメーバ25
    # 25: アメーバ26
    # 26: アメーバ27
    # 27: アメーバ28
    # 28: アメーバ29
    # 29: アメーバ30
    # 30: アメーバ31
    # 31: アメーバ32
    # 32: アメーバ33
    # 33: アメーバ34
    # 34: アメーバ35
    # 35: アメーバ36
    # 36: アメーバ37
    # 37: アメーバ38
    # 38: アメーバ39
    # 39: アメーバ40
    # 40: アメーバ41
    # 41: ア

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    
    B = [0] * (2*N+2)
    for i in range(1, N+1):
        B[i] = A[i]
        B[i*2] = A[i]
        B[i*2+1] = A[i]
    
    #print(B)
    
    for i in range(1, 2*N+2):
        cnt = 0
        while B[i] != 1:
            #print(B[i])
            B[i] = B[int(B[i]/2)]
            cnt += 1
        print(cnt)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*(2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(2*N,0,-1):
        ans[i//2] = max(ans[i//2], ans[i]+1)
    for i in range(1,2*N+1):
        print(ans[i])

=======
Suggestion 8

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans_list = [0] * (2*n+1)
    ans_list[1] = 0
    for i in range(n):
        ans_list[2*i+2] = i+1
        ans_list[2*i+3] = i+1
    for i in range(2*n-1, 0, -1):
        ans_list[i//2] = ans_list[i] + 1
    for ans in ans_list:
        print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1

    for i in range(2 * n, 0, -1):
        if ans[i] == 0:
            ans[i] = ans[2 * i] + ans[2 * i + 1]
    for i in range(1, 2 * n + 1):
        print(ans[i])
