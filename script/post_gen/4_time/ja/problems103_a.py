Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    A1, A2, A3 = map(int, input().split())

    # compute

    # output
    print(min(abs(A1-A2)+abs(A2-A3), abs(A1-A3)+abs(A3-A2), abs(A2-A1)+abs(A1-A3)))

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 3

def main():
    # input
    A1, A2, A3 = map(int, input().split())
    # compute
    # output
    print(max(A1, A2, A3) - min(A1, A2, A3))

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[1]-A[0])+abs(A[2]-A[1]))

=======
Suggestion 5

def main():
    # 自分の解答
    # a = list(map(int, input().split()))
    # a.sort()
    # print(a[2]-a[0])

    # 解答例1
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 6

def main():
    #input
    a = list(map(int, input().split()))

    #compute
    a.sort()
    cost = a[2] - a[0] - a[1]

    #output
    print(cost)

=======
Suggestion 7

def main():
    # データ入力
    a = list(map(int, input().split()))
    # 処理
    # ソート
    a.sort()
    # 出力
    print(a[2] - a[0])
