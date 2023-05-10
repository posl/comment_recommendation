Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        a_i = a[i]
        if len(ans) == 0:
            ans.append(a_i)
            continue
        if ans[-1] == a_i:
            ans.pop()
        else:
            ans.append(a_i)
    print(len(ans))

=======
Suggestion 2

def main():
    N = int(input())
    balls = [int(x) for x in input().split()]
    count = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        count[balls[i]] += 1
    for i in range(1, 2 * 10 ** 5 + 1):
        count[i] += count[i - 1]
    for i in range(N):
        print(count[balls[i] - 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    B = [0] * N
    #print(B)
    for i in range(N):
        B[A[i]-1] += 1
    #print(B)
    for i in range(N):
        print(B[i])

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    #print(len(A))
    #print(A[0])
    #

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5):
        if b[i] == 0:
            continue
        if b[i] >= i:
            ans += b[i] - i
        else:
            ans += b[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))

    # 初期状態
    balls = []
    for i in range(N):
        balls.append(0)

    # ボールを落とす
    for i in range(N):
        balls[a[i]-1] += 1

    # 筒の中に何個のボールがあるか求める
    for i in range(N):
        print(balls[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))

    # 2以上の整数が書かれたN個のボールを持っており、これらを細長い筒の中に落としていく
    # i回目には、a_iが書かれたボールを落とす
    # ボールは特殊な材質でできており、筒の中においてkが書かれたボールがk個連続すると、それらk個のボールは全て消えてしまう
    # 各iについて、i個目のボールを筒の中に落とした後、筒の中に何個のボールがあるか求める

    # 1~N回目のボールを落とす
    # 筒の中にあるボールに書かれた整数は、下から順に3, 2, 3, 2, 2となるが、2が書かれたボールが2個連続しているのでこれらは消え、下から順に3, 2, 3となる

    # N = 5
    # a = [3, 2, 3, 2, 2]
    # a = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]

    # 1回目
    # 3
    # 2回目
    # 3, 2
    # 3回目
    # 3, 2, 3
    # 4回目
    # 3, 2, 3, 2
    # 5回目
    # 3, 2, 3, 2, 2
    # 2が書かれたボールが2個連続しているのでこれらは消え、下から

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        a[i] -= 1
        if i == 0:
            ans.append(1)
            continue
        if a[i] == a[i-1]:
            ans.append(ans[i-1]+1)
        else:
            ans.append(1)
    for j in ans:
        print(j)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # 連続している数字の個数
    cnt = 0
    for i in range(N):
        # 筒の中にあるボールに書かれた整数は下から順に 3, 2, 3, 2, 2 となるが、2 が書かれたボールが 2 個連続しているのでこれらは消え、下から順に 3, 2, 3 となる。
        # 連続している数字の個数が2以上の場合、消える
        if cnt >= 2:
            # 連続している数字の個数を0にする
            cnt = 0
            # 消えるので筒の中のボールの個数を-1する
            ans -= 1
        # 連続している数字の個数を1つ増やす
        cnt += 1
        # 筒の中のボールの個数を1つ増やす
        ans += 1
    print(ans)
    return 0
