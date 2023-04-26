Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*(2*N+1)
    for i in range(N):
        ans[2*i+1] = ans[A[i]-1]+1
        ans[2*i+2] = ans[A[i]-1]+1
    for i in range(2*N+1):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[2*i] = ans[2*i+1] = ans[A[i]] + 1
    print(*ans, sep='

')

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    parent = [0] * (2*N+1)
    for i in range(N):
        a = A[i]
        parent[2*i+1] = a
        parent[2*i+2] = a
    for i in range(2*N+1):
        if parent[i] == 0:
            break
        parent[i] = parent[parent[i]-1]
    for i in range(2*N+1):
        print(parent[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*(2*N+1)
    for i in range(N):
        ans[2*(i+1)-1] = ans[A[i]-1] + 1
        ans[2*(i+1)] = ans[A[i]-1] + 1
    for i in range(2*N+1):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = 1
        ans[2 * A[i]] = ans[2 * A[i] + 1] = ans[A[i]] + 1
    for i in range(2 * N + 1):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [1, 3, 5, 2]
    # N = 4
    # A = [1, 2]
    # N = 2
    # A = [1, 3, 5, 2]
    # N = 4
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # N = 10
    # A = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    # N = 10
    # A = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    # N = 10
    # A = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    # N = 10
    # A = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    # N = 10
    # A = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    # N = 10
    # A = [1, 3, 5, 2, 4, 6, 8, 10, 7, 9]
    # N = 10

    # 2N+1行出力せよ。k 行目にはアメーバ k から何代親を遡るとアメーバ 1 になるかを出力せよ。
    # 2N+1行出力せよ。k 行目にはアメーバ k から何代親を遡るとアメーバ 1 になるかを出力せよ。
    # 2N+1行出力せよ。k 行目にはアメーバ k から何

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2N+1の配列を用意
    ans = [0] * (2 * N + 1)
    # Aの要素を1から順に見ていく
    for i in range(N):
        # A[i]の親はA[i]の2倍-1を2で割ったもの
        parent = (A[i] * 2 - 1) // 2
        # A[i]の親はA[i]の2倍-1を2で割ったもの
        ans[A[i] * 2 - 1] = ans[parent] + 1
        # A[i]の親はA[i]の2倍を2で割ったもの
        ans[A[i] * 2] = ans[parent] + 1
    for i in range(2 * N + 1):
        print(ans[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #親の番号を格納するリスト
    parent = [0]*(2*N+1)
    #アメーバの世代を格納するリスト
    generation = [0]*(2*N+1)
    #親の番号を格納する
    for i in range(N):
        parent[2*i+1] = A[i]
        parent[2*i+2] = A[i]
    #アメーバの世代を格納する
    for i in range(2*N+1):
        if i == 0:
            generation[i] = 0
        else:
            generation[i] = generation[parent[i]-1] + 1
    #アメーバの世代を出力する
    for i in range(2*N+1):
        print(generation[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #親のリスト
    parent = [0]*(2*N+1)
    #親のリストを作成
    for i in range(N):
        parent[2*i+1] = A[i]
        parent[2*i+2] = A[i]

    #親のリストから何代親かを求める
    for i in range(2*N+1):
        if parent[i] == 0:
            print(0)
        else:
            count = 0
            while parent[i] != 1:
                i = parent[i]-1
                count += 1
            print(count+1)
