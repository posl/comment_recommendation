Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    m = 0
    for i in range(1, n):
        if h[i] <= h[i-1]:
            m += 1
        else:
            ans = max(ans, m)
            m = 0
    ans = max(ans, m)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

=======
Suggestion 4

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            tmp += 1
        else:
            tmp = 0
        if tmp > ans:
            ans = tmp
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    ans = 0
    for i in range(1,n):
        if h[i-1] >= h[i]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)

=======
Suggestion 9

def main():
    # 標準入力からNを取得する
    n = int(input())

    # 標準入力からHを取得する
    h = list(map(int, input().split()))

    # 計算処理
    # 右隣のマスの高さが今居るマスの高さ以下である限り右隣のマスへ移動し続けます。
    # 最大で何回移動できるでしょうか。
    # 左から i 番目のマスの高さは H_i です。

    # 右隣のマスの高さが今居るマスの高さ以下である限り右隣のマスへ移動し続けます。
    # 最大で何回移動できるでしょうか。
    # 左から i 番目のマスの高さは H_i です。

    # とりあえず、最初のマスに降り立つとして、右隣のマスの高さが今居るマスの高さ以下である限り右隣のマスへ移動し続けます。
    # ということは、右隣のマスの高さが今居るマスの高さ以下でなくなったら、そこで止まる。
    # ということは、右隣のマスの高さが今居るマスの高さ以下でなくなったら、そこで止まる。
    # ということは、右隣のマスの高さが今居るマスの高さ以下でなくなったら、そこで止まる。
    # ということは、右隣のマスの高さが今居るマスの高さ以下でなくなったら、そこで止まる。
    # ということは、右隣のマスの高さが今居るマスの高さ

=======
Suggestion 10

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)
