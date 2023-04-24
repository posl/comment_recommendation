Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if a[i] == a[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = 1
    for i in range(N):
        if ans[i] % 2 == 0:
            print(ans[i] // 2)
        else:
            print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        cnt[a[i]] += 1
        if cnt[a[i]] == a[i]:
            print(i + 1)
            return
        else:
            print(i + 1 - cnt[a[i]] + 1)

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ball = []
    for i in range(N):
        ball.append(a[i])
        if len(ball) >= 2:
            if ball[-1] == ball[-2]:
                ball.pop()
                ball.pop()
    print(N - len(ball))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    balls = [0] * (2*10**5+1)
    for a in A:
        balls[a] += 1
        print(sum(balls))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 筒の中にあるボールの個数
    cnt = 0
    # 筒の中にあるボールの個数を記録する配列
    ans = []
    for i in range(N):
        # 筒の中にあるボールの個数を記録する配列に追加
        ans.append(cnt)
        # 筒の中にあるボールの個数を更新
        if cnt == 0:
            cnt = 1
        else:
            if A[i] == A[i-1]:
                cnt += 1
            else:
                cnt = 1

        # 筒の中にあるボールの個数が2の倍数の時、ボールを消す
        if cnt % 2 == 0:
            cnt -= 2

    # 筒の中にあるボールの個数を記録する配列に追加
    ans.append(cnt)

    # 筒の中にあるボールの個数を出力
    for i in range(N+1):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if A[i] == cnt:
            ans[i] = ans[i-1] - 1
            cnt = 0
        else:
            ans[i] = ans[i-1] + 1
            cnt = A[i]
    print(*ans, sep='

')

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 筒の中にあるボールの個数
    ball_num = 0
    # 筒の中にあるボールの個数を記録するリスト
    ball_num_list = [0] * N
    # 筒の中にあるボールの個数の前回の値
    prev_ball_num = 0
    # 筒の中にあるボールの個数の前回の値を記録するリスト
    prev_ball_num_list = [0] * N
    # 筒の中にあるボールの個数を記録するリストのインデックス
    i = 0
    for a in A:
        # 筒の中にあるボールの個数の前回の値を記録するリストに記録
        prev_ball_num_list[i] = prev_ball_num
        # ボールの個数の前回の値を更新
        prev_ball_num = ball_num
        # ボールの個数を更新
        ball_num += 1
        # ボールの個数がボールに書かれた整数と同じならば
        if ball_num == a:
            # ボールの個数を 0 に更新
            ball_num = 0
        # 筒の中にあるボールの個数を記録するリストに記録
        ball_num_list[i] = ball_num
        # ボールの個数を記録するリストのインデックスを更新
        i += 1
    # 筒の中にあるボールの個数を記録するリストのインデックスを 0 にリセット
    i = 0
    for a in A:
        # 筒の中にあるボールの個数の前回の値を記録するリストの値を

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    cnt = 1
    for i in range(N):
        if A[i] == cnt:
            cnt += 1
        else:
            print(cnt)
    print(cnt)
    return

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if A[i] == 2:
            if ans[i-1] == 1:
                ans[i] = 2
            else:
                ans[i] = 1
        else:
            if ans[i-1] == 0:
                ans[i] = 1
            else:
                ans[i] = 0
    print(*ans, sep='

')

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if count == 0:
            count += 1
            print(count)
            continue
        if a[i] == a[i-1]:
            count += 1
            print(count)
        else:
            count = 1
            print(count)
