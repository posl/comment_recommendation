Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (w + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(w, -1, -1):
            if j + a[i] <= w:
                dp[j + a[i]] += dp[j]
    print(sum(dp))

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (sum(A) + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(sum(A), A[i] - 1, -1):
            if dp[j - A[i]]:
                dp[j] = 1
    ans = 0
    for i in range(len(dp)):
        if dp[i] and i <= W:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (w + 1)
    for i in range(n):
        for j in range(w, a[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - a[i]] + a[i])
    print(dp[w])

=======
Suggestion 4

def main():
    n,w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(2**n):
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += a[j]
        if s <= w:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # W以下の良い整数の個数を数える
    # 重さの和の最大値は W なので、W+1個の0を持つリストを用意する
    dp = [0] * (W+1)
    # おもりの重さの和が0のときは1通り
    dp[0] = 1
    # おもりの重さの和の最大値は W なので、W+1個の0を持つリストを用意する
    dp2 = [0] * (W+1)
    # おもりの重さの和が0のときは1通り
    dp2[0] = 1
    # おもりを1つずつ見ていく
    for i in range(N):
        # おもりの重さ
        a = A[i]
        # おもりの重さの和の最大値は W なので、W+1個の0を持つリストを用意する
        dp3 = [0] * (W+1)
        # おもりの重さの和が0のときは1通り
        dp3[0] = 1
        # おもりの重さの和の最大値は W なので、W+1個の0を持つリストを用意する
        dp4 = [0] * (W+1)
        # おもりの重さの和が0のときは1通り
        dp4[0] = 1
        # おもりの重さの和の最大値は W なので、W+1個の0を持つリストを用意する
        dp5 = [0] * (W+1)
        # おもりの重さの和が0のときは1通り
        dp5[0] =

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])
    # print(A[9])
    # print(A[10])
    # print(A[11])
    # print(A[12])
    # print(A[13])
    # print(A[14])
    # print(A[15])

    # 3 個以下の異なるおもりを自由に選んで、選んだおもりの重さの和を n にすることができる。
    # W 以下の正整数のうち、良い整数は何個ありますか？
    # N 個のおもりの重さの和の最大値は 10^6 * 300 = 3000000 なので、
    # 3000000 以下の正整数のうち、良い整数は何個あるかを求める。
    # 3000000 以下の正整数のうち、良い整数は何個あるかを求める。
    # おもりが 1 個のときは 3000000 以下の正整数のうち、良い整数は何個あるかを求める。
    # おもりが 2 個のときは 3000000 以下の正整数のうち、良い整数は何個あるかを求める。
    # おもりが 3 個のときは 3000000 以下の正整数のうち、良い整数は何個あるかを求める。
    # おもりが 4 個のときは 3000000 以下の正整数のうち、良い

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    #print(A)
    #print(N, W)

=======
Suggestion 8

def main():
    # おもりの数
    N = int(input())
    # おもりの重さ
    W = int(input())
    # おもりの重さをリストに格納
    A = list(map(int, input().split()))
    # 良い整数の個数
    count = 0
    # おもりの重さの和
    sum = 0
    # おもりの重さの和を格納するリスト
    sum_list = []
    # おもりの重さの和を格納するリストに0を追加
    sum_list.append(0)
    # おもりの重さの和を格納するリストに1を追加
    sum_list.append(1)

    # おもりの重さの和を格納するリストを作成
    for i in range(N):
        sum += A[i]
        sum_list.append(sum)

    # おもりの重さの和を格納するリストの中から、
    # 重さの和がW以下のものをカウント
    for i in sum_list:
        if i <= W:
            count += 1

    print(count)

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(N, W)
    # print(A)

    # A1を選ぶときの重さの和のリスト
    A1 = [0]
    for i in range(N):
        tmp = []
        for j in A1:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A1.extend(tmp)
    A1.sort()
    # print(A1)

    # A2を選ぶときの重さの和のリスト
    A2 = [0]
    for i in range(N):
        tmp = []
        for j in A2:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A2.extend(tmp)
    A2.sort()
    # print(A2)

    # A1を選ぶときの重さの和のリスト
    A3 = [0]
    for i in range(N):
        tmp = []
        for j in A3:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A3.extend(tmp)
    A3.sort()
    # print(A3)

    # A1を選ぶときの重さの和のリスト
    A4 = [0]
    for i in range(N):
        tmp = []
        for j in A4:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A4.extend(tmp)
    A4.sort()
    # print(A4)

    # A1を選ぶときの重さの和のリスト
    A5 = [0]
    for i in range(N):
        tmp = []
        for j in A5:
            if j + A[i] <= W:
                tmp.append(j + A[i])
        A5.extend(tmp)
    A5.sort()
    # print(A5)

    # A1を選ぶときの重さの和のリスト
    A6 = [0]
    for i in range(N):
        tmp = []
        for j in A6:
            if j + A[i] <= W:
                tmp.append(j
