Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if X == A[X-1]:
            cnt += 1
            break
        else:
            X = A[X-1]
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    X -= 1
    ans = 0
    visited = [False] * N
    while not visited[X]:
        visited[X] = True
        X = A[X]
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    ans = 0
    X = A[X]
    while X != 1:
        ans += 1
        X = A[X]
    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    cnt = 1
    next = X
    while True:
        if A[next] == X:
            break
        next = A[next]
        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    ans = 0
    d = set()
    while True:
        if x in d:
            print(-1)
            return
        if x == 1:
            print(ans)
            return
        d.add(x)
        x = a[x] - 1
        ans += 1

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    count = 0
    a = X-1
    while True:
        a = A[a]
        count += 1
        if a == X-1:
            break
    print(count)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    #print(A)
    #print(A[X])
    #print(A[A[X]])
    #print(A[A[A[X]]])

    ans = 0
    ans_list = []
    ans_list.append(X)
    ans_list.append(A[X])
    ans_list.append(A[A[X]])
    ans_list.append(A[A[A[X]]])

    #print(ans_list)

    for i in range(4, N+1):
        if A[ans_list[i-1]] in ans_list:
            ans = i
            break
        else:
            ans_list.append(A[ans_list[i-1]])
            #print(ans_list)
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # print(N, X)
    # print(A)
    # print(A[X-1])
    # print(A[A[X-1]-1])
    # print(A[A[A[X-1]-1]-1])
    # print(A[A[A[A[X-1]-1]-1]-1])
    # print(A[A[A[A[A[X-1]-1]-1]-1]-1])
    # print(A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1])
    # print(A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1])
    # print(A[A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1]-1])
    # print(A[A[A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1]-1]-1])
    # print(A[A[A[A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1]-1]-1]-1])

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, X)
    #print(A)

    #友達の数Nと、友達Xの位置を取得
    #友達のリストAを取得
    #print(A[X-1])
    #print(A[X-1])
    #print(A[X-1])
    #print(A[X-1])

    #友達Xの位置を取得
    #友達Xの位置の友達番号を取得
    #友達番号の友達番号を取得
    #友達番号の友達番号の友達番号を取得
    #友達番号の友達番号の友達番号の友達番号を取得
    #友達番号の友達番号の友達番号の友達番号の友達番号を取得
    #友達番号の友達番号の友達番号の友達番号の友達番号の友達�

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # Xの値を0から始めるために1を引く
    X -= 1
    # 0からNまでのリストを作成
    # 0:未知, 1:知っている, 2:知られている
    ans = [0] * N
    # Xの友達は知っている
    ans[X] = 1
    # Xの友達を知っている人数
    cnt = 1
    # Xの友達の友達を知っている人数
    cnt2 = 0
    # Xの友達の友達を知っている人数が0になるまで繰り返す
    while cnt2 != 0:
        # Xの友達の友達を知っている人数を0にする
        cnt2 = 0
        # Xの友達の友達を知っている人数を数える
        for i in range(N):
            if ans[i] == 2:
                cnt2 += 1
        # Xの友達の友達を知っている人数が0になったら終了
        if cnt2 == 0:
            break
        # Xの友達の友達を知っている人数を0にする
        cnt2 = 0
        # Xの友達の友達を知っている人数を数える
        for i in range(N):
            if ans[i] == 2:
                cnt2 += 1
        # Xの友達の友達を知っている人数が0になったら終了
        if cnt2 == 0:
            break
        # Xの友達の友達を知っている人数を0にする
        cnt2 = 0
        # Xの友達の友達を知っている人数を数える
        for i in range
