Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    sum = 0
    for i in range(1, 10**9):
        sum += i
        if sum >= N:
            print(i)
            break

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    i = 1
    while sum < n:
        sum += i
        i += 1
    print(i-1)

=======
Suggestion 3

def main():
    N = int(input())
    i = 0
    sum = 0
    while sum < N:
        i += 1
        sum += i
    print(i)

main()

=======
Suggestion 4

def main():
    n = int(input())
    i = 1
    sum = 0
    while sum < n:
        sum += i
        i += 1
    print(i-1)

=======
Suggestion 5

def main():
    N = int(input())
    day = 0
    total = 0
    while total < N:
        day += 1
        total += day
    print(day)

=======
Suggestion 6

def main():
    N = int(input())
    # 1日目の朝に1円、2日目の朝に2円...というようにi日目の朝にi円を貯金箱に入れる。
    # また、毎日夜に貯金箱にいくら入っているかを確認する。
    # 貯金箱にN円以上入っていることを初めて確認するのは、何日目の夜でしょうか?
    # 1 ≦ N ≦ 10^9

    # 1日目の朝に1円、2日目の朝に2円...というようにi日目の朝にi円を貯金箱に入れる。
    # また、毎日夜に貯金箱にいくら入っているかを確認する。
    # 貯金箱にN円以上入っていることを初めて確認するのは、何日目の夜でしょうか?
    # 1 ≦ N ≦ 10^9

    # N円以上入るのは、N円を超える日の朝に入れると、その日の夜にN円以上入っていることになる
    # そのため、N円を超える日の朝に入れる日を求めれば良い

    # 1日目の朝に1円、2日目の朝に2円...というようにi日目の朝にi円を貯金箱に入れる。
    # また、毎日夜に貯金箱にいくら入っているかを確認する。
    # 貯金箱にN円以上入っていることを初めて確認するのは、何日目の夜でしょうか?
    # 1 ≦ N ≦ 10^9

    # N円以上入るのは、N円を超

=======
Suggestion 7

def main():
    N = int(input())
    if N == 1:
        print(1)
    else:
        a = 0
        for i in range(1,N):
            a += i
            if N <= a:
                print(i)
                break

=======
Suggestion 8

def main():
    N = int(input())
    #貯金箱の中身
    box = 0
    #貯金箱に入れた金額
    money = 0
    #何日目か
    day = 0
    while box < N:
        day += 1
        money += day
        box += money
    print(day)

=======
Suggestion 9

def main():
    N = int(input())
    #貯金箱に入っているお金
    box = 0
    #何日目の夜か
    day = 0
    while True:
        day += 1
        box += day
        if box >= N:
            break
    print(day)
