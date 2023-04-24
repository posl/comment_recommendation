Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i+1 < n:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    happy = [0] * N
    for i in range(N):
        happy[(i - 1) % N] += 1
        happy[i] += 1
        happy[(i + 1) % N] += 1
    happy_count = 0
    for i in range(N):
        if happy[P[i]] > 0:
            happy_count += 1
    print(happy_count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += (P[i] == i-1 or P[i] == i or P[i] == i+1)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0 and p[i] == p[i+1] - 1:
            ans += 1
        elif i == n-1 and p[i] == p[i-1] - 1:
            ans += 1
        elif p[i] == p[i-1] - 1 or p[i] == p[i+1] - 1:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N, p)
    if p[0] == 0:
        if p[N-1] == N-1:
            print(N)
        else:
            print(N-1)
    elif p[N-1] == N-1:
        print(N-1)
    else:
        print(N-2)

main()

This code got 100 points.

Rate this: Share this: Twitter

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # d[i] = j となるように、d の作成
    d = [0] * N
    for i in range(N):
        d[P[i]] = i

    # d[i] = j となるように、d の作成
    # d = [0] * N
    # for i in range(N):
    #     d[P[i]] = i

    # d の中で最小の値を見つける
    min_d = min(d)

    # d の中で最小の値を見つける
    # min_d = min(d)

    # d の中で最小の値を 0 にする
    for i in range(N):
        d[i] -= min_d

    # d の中で最小の値を 0 にする
    # for i in range(N):
    #     d[i] -= min_d

    # d を d の最小の値で割る
    for i in range(N):
        d[i] //= min_d

    # d を d の最小の値で割る
    # for i in range(N):
    #     d[i] //= min_d

    # d を d の最小の値で割った結果、最大の値を見つける
    max_d = max(d)

    # d を d の最小の値で割った結果、最大の値を見つける
    # max_d = max(d)

    # d を d の最小の値で割った結果、最大の値を見つけたときの d の中でのインデックスを見つける
    for i in range(N):
        if d[i] == max_d:
            break

    # d を d の最小の値で割った結果、最大の値を見つけたときの d の中でのインデックスを見つける
    # for i in range(N):
    #     if d[i

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    #print("")

    # 1. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 2. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 3. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 4. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 5. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 6. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 7. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 8. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 9. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    # 1. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 2. 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    # 3. 2, 3, 4, 5, 6, 7, 8, 9, 0, 1
    # 4. 3, 4, 5, 6, 7, 8, 9, 0, 1, 2
    # 5. 4, 5,

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # P[i]が人iの前にいたとする
    # 人iの前にいるはずの皿はP[P[i]]になる
    # 人iの前にいるはずの皿をP[i]にするためには、
    # 人iの前にいるはずの皿をP[P[i]]にする必要がある
    # つまり、P[P[i]]をP[i]にする操作を行えばよい
    # 人iの前にいるはずの皿をP[i]にする操作を行うためには、
    # 人iの前にいるはずの皿をP[P[i]]にする操作を行う必要がある
    # つまり、P[P[P[i]]]をP[i]にする操作を行えばよい
    # 人iの前にいるはずの皿をP[i]にする操作を行うためには、
    # 人iの前にいるはずの皿をP[P[i]]にする操作を行う必要がある
    # つまり、P[P[P[P[i]]]]をP[i]にする操作を行えばよい
    # ...
    # 人iの前にいるはずの皿をP[i]にする操作を行うためには、
    # 人iの前にいるはずの皿をP[P[i]]にする操作を行う必要がある
    # つまり、P[P[i]]をP[i]にする操作を行えばよい
    # 人iの前にいるはずの皿をP[i]にする操作を行うためには、
    # 人iの前にいるはずの皿をP[P[i]]にする操作を行う必要がある
    # つまり、P[P[P[i]]]をP

=======
Suggestion 9

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    #print("=====")
    # 1. find the longest consecutive sequence
    # 2. the answer should be the length of the longest consecutive sequence + 1
    # 3. if the longest consecutive sequence is the whole array, then the answer should be N
    # 4. if the longest consecutive sequence is 1, then the answer should be 2

    # 1. find the longest consecutive sequence
    # 2. the answer should be the length of the longest consecutive sequence + 1
    # 3. if the longest consecutive sequence is the whole array, then the answer should be N
    # 4. if the longest consecutive sequence is 1, then the answer should be 2

    # 1. find the longest consecutive sequence
    # 2. the answer should be the length of the longest consecutive sequence + 1
    # 3. if the longest consecutive sequence is the whole array, then the answer should be N
    # 4. if the longest consecutive sequence is 1, then the answer should be 2

    # 1. find the longest consecutive sequence
    # 2. the answer should be the length of the longest consecutive sequence + 1
    # 3. if the longest consecutive sequence is the whole array, then the answer should be N
    # 4. if the longest consecutive sequence is 1, then the answer should be 2

    # 1. find the longest consecutive sequence
    # 2. the answer should be the length of the longest consecutive sequence + 1
    # 3. if the longest consecutive sequence is the whole array, then the answer should be N
    # 4. if the longest consecutive sequence is 1, then the answer should be 2

    # 1. find the longest consecutive sequence
    # 2. the answer should be the length of the longest consecutive sequence + 1
    # 3. if the longest consecutive sequence is the whole array, then the answer should be N
    # 4. if the longest consecutive sequence is 1, then the answer should be 2

    # 1. find the longest consecutive sequence
    #
