Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = 1
        ans[2 * i + 1] = ans[A[i]] + 1
        ans[2 * i + 2] = ans[A[i]] + 1
    for i in range(2 * N + 1):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    parent = [0] * (2 * N + 1)
    for i in range(N):
        parent[2 * i + 1] = A[i]
        parent[2 * i + 2] = A[i]
    for i in range(2 * N + 1):
        if parent[i] == 0:
            print(0)
        else:
            count = 1
            while parent[i] != 1:
                parent[i] = parent[parent[i]]
                count += 1
            print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[2*i] = ans[A[i]-1] + 1
        ans[2*i+1] = ans[A[i]-1] + 1
        ans[A[i]-1] += 1
    for i in range(2*N+1):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[A[i]] = 1
        ans[2*i+1] = ans[2*i+2] = ans[A[i]] + 1
    for i in range(2*N+1):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[2*i+1] = ans[A[i]-1] + 1
        ans[2*i+2] = ans[A[i]-1] + 1
    for i in range(2*N+1):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[A[i]-1] = min(ans[A[i]-1], i)
        ans[2*i] = min(ans[2*i], i+1)
        ans[2*i+1] = min(ans[2*i+1], i+1)
    for i in range(2*N+1):
        print(ans[i])

=======
Suggestion 7

def main():
    N=int(input())
    A=list(map(int,input().split()))
    B = [0] * (2*N+1)
    for i in range(N):
        B[2*i+1] = A[i]
        B[2*i+2] = A[i]
    for i in range(2*N,0,-1):
        if i%2==1:
            B[i//2] = B[i]
    for i in range(2*N+1):
        print(B[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # アメーバの親を記録する配列
    parents = [0] * (2 * n + 2)

    # 親を記録
    for i in range(n):
        parents[2 * i + 1] = a[i]
        parents[2 * i + 2] = a[i]

    # 各アメーバの親を辿ってアメーバ1になるまでの距離を計算
    for i in range(2, 2 * n + 2):
        parents[i] = parents[parents[i]] + 1

    # 計算結果を出力
    for i in range(1, 2 * n + 2):
        print(parents[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A:観察記録
    # A[i]:i番目の観察記録で、親の番号
    # A[i] = 2i-1,2i はありえない
    # A[i] = 2j+1,2j+2 はありえない
    # A[i] = 2j,2j+1 はありえる
    # A[i] = 2j,2j+2 はありえる
    # A[i] = 2j+1,2j+3 はありえる
    # A[i] = 2j+2,2j+3 はありえる
    # A[i] = 2j+1,2j+2 はありえない
    # A[i] = 2j+2,2j+1 はありえない

    # 答えを格納するリスト
    ans = []
    # 2N+1個のアメーバの親を格納するリスト
    parent = [0] * (2*N+1)
    # 2N+1個のアメーバの親を格納するリスト
    parent[1] = 1
    # 2N+1個のアメーバの何代親を格
