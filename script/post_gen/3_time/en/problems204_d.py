Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) + max(T) // 2)

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(sum(T) - max(T) // 2)

=======
Suggestion 3

def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(sum(t) - max(t) // 2)

main()

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = T[0]
    for i in range(1,N):
        ans += T[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    t = [int(x) for x in input().split()]
    t.sort()
    ans = t[0]
    for i in range(1,n):
        ans += t[i]
    ans -= t[0]//2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    T = [int(_) for _ in input().split()]
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

=======
Suggestion 7

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    else:
        print(sum(T) - (T[0] / 2))

=======
Suggestion 8

def oven():
    # N個の料理を作る
    N = int(input())
    # T_iはi番目の料理の焼く時間
    T = list(map(int, input().split()))
    # 一番時間がかかる料理の時間を求める
    max_time = max(T)
    # 一番時間がかかる料理の時間を除いた残りの料理の時間を求める
    T.remove(max_time)
    # 一番時間がかかる料理の時間と残りの料理の時間の合計を求める
    total_time = max_time + sum(T)
    # 一番時間がかかる料理の時間と残りの料理の時間の合計を出力する
    print(total_time)

oven()
