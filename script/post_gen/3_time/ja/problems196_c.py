Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        i = str(i)
        if len(i)%2 == 0:
            if i[:len(i)//2] == i[len(i)//2:]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, 12):
        for j in range(10**(i-1), 10**i):
            if j > N:
                break
            if len(str(j))%2 == 0:
                if str(j)[:len(str(j))//2] == str(j)[len(str(j))//2:]:
                    ans += 1
    print(ans)

main()

=======
Suggestion 3

def solve(n):
    if n < 11:
        return 0
    if n < 111:
        return 9
    if n < 1111:
        return 9 + 9
    if n < 11111:
        return 9 + 9 + 90
    if n < 111111:
        return 9 + 9 + 90 + 900
    if n < 1111111:
        return 9 + 9 + 90 + 900 + 9000
    if n < 11111111:
        return 9 + 9 + 90 + 900 + 9000 + 90000
    if n < 111111111:
        return 9 + 9 + 90 + 900 + 9000 + 90000 + 900000
    if n < 1111111111:
        return 9 + 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000
    if n < 11111111111:
        return 9 + 9 + 90 + 900 + 9000 + 90000 + 900000 + 9000000 + 90000000

=======
Suggestion 4

def main():
    N = int(input())
    if N < 10:
        print(N)
        return
    if N < 100:
        print(N-9)
        return
    if N < 1000:
        print(N-9)
        return
    if N < 10000:
        print(N-99)
        return
    if N < 100000:
        print(N-99)
        return
    if N < 1000000:
        print(N-999)
        return
    if N < 10000000:
        print(N-999)
        return
    if N < 100000000:
        print(N-9999)
        return
    if N < 1000000000:
        print(N-9999)
        return
    if N < 10000000000:
        print(N-99999)
        return
    if N < 100000000000:
        print(N-99999)
        return
    if N < 1000000000000:
        print(N-999999)
        return

=======
Suggestion 5

def main():
    N = int(input())
    # 1桁
    if N < 10:
        print(0)
        return
    # 2桁
    if N < 100:
        print(9)
        return
    # 3桁
    if N < 1000:
        print(9)
        return
    # 4桁
    if N < 10000:
        print(9*2)
        return
    # 5桁
    if N < 100000:
        print(9*3)
        return
    # 6桁
    if N < 1000000:
        print(9*4)
        return
    # 7桁
    if N < 10000000:
        print(9*5)
        return
    # 8桁
    if N < 100000000:
        print(9*6)
        return
    # 9桁
    if N < 1000000000:
        print(9*7)
        return
    # 10桁
    if N < 10000000000:
        print(9*8)
        return
    # 11桁
    if N < 100000000000:
        print(9*9)
        return
    # 12桁
    if N < 1000000000000:
        print(9*10)
        return
    # 13桁
    if N < 10000000000000:
        print(9*11)
        return
    # 14桁
    if N < 100000000000000:
        print(9*12)
        return

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        s = str(i)
        if len(s) % 2 == 0:
            if int(s[:len(s)//2]) <= N:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**6+1):
        s = str(i)
        if len(s) % 2 == 0:
            a = s[:len(s)//2]
            b = s[len(s)//2:]
            if a == b:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    #N = 10000000
    #N = 33
    #N = 1333
    #N = 1000000000000
    #N = 10000000000000
    #N = 100000000000000

    # 1桁の数は条件を満たさない
    if N < 10:
        print(0)
        return

    # 1桁の数は条件を満たさない
    if N < 100:
        print(1)
        return

    # 1桁の数は条件を満たさない
    if N < 1000:
        print(9)
        return

    # 1桁の数は条件を満たさない
    if N < 10000:
        print(9 + 9)
        return

    # 1桁の数は条件を満たさない
    if N < 100000:
        print(9 + 9 + 9)
        return

    # 1桁の数は条件を満たさない
    if N < 1000000:
        print(9 + 9 + 9 + 9)
        return

    # 1桁の数は条件を満たさない
    if N < 10000000:
        print(9 + 9 + 9 + 9 + 9)
        return

    # 1桁の数は条件を満たさない
    if N < 100000000:
        print(9 + 9 + 9 + 9 + 9 + 9)
        return

    # 1桁の数は条件を満たさない
    if N < 1000000000:
        print(9 + 9 + 9 + 9 + 9 + 9 + 9)
        return

    # 1桁の数は条件を満たさない
    if N < 10000000000:
        print(9 + 9 + 9 + 9 + 9 + 9 + 9 + 9)
        return

    # 1桁

=======
Suggestion 9

def main():
    N = int(input())
    # N = 10000000
    # N = 1333
    # N = 33
    # N = 1
    # N = 0
    # N = 1000000000000

    # 1桁の場合
    if N < 10:
        print(N)
        return

    # 2桁の場合
    if N < 100:
        print(N - 9)
        return

    # 3桁の場合
    if N < 1000:
        print(N - 9)
        return

    # 4桁の場合
    if N < 10000:
        print(N - 9)
        return

    # 5桁の場合
    if N < 100000:
        print(N - 9)
        return

    # 6桁の場合
    if N < 1000000:
        print(N - 9)
        return

    # 7桁の場合
    if N < 10000000:
        print(N - 9)
        return

    # 8桁の場合
    if N < 100000000:
        print(N - 9)
        return

    # 9桁の場合
    if N < 1000000000:
        print(N - 9)
        return

    # 10桁の場合
    if N < 10000000000:
        print(N - 9)
        return

    # 11桁の場合
    if N < 100000000000:
        print(N - 9)
        return

    # 12桁の場合
    if N < 1000000000000:
        print(N - 9)
        return

    # 13桁の場合
    if N < 10000000000000:
        print(N - 9)
        return

    # 14桁の場合
    if N < 100000000000000:
        print(N - 9)
        return

    # 15桁の場合
    if N < 1000000000000000:
        print(N - 9)
        return

    # 16桁

=======
Suggestion 10

def main():
    N = int(input())
    # 99を超えると10桁になるので、それまでの数値を計算する
    # 1桁目は2桁目と同じ数値、2桁目は3桁目と同じ数値・・・となる
    # 1桁目は1,2,3,4,5,6,7,8,9の9通り
    # 2桁目は1,2,3,4,5,6,7,8,9の9通り
    # 3桁目は1,2,3,4,5,6,7,8,9の9通り
    # 4桁目は1,2,3,4,5,6,7,8,9の9通り
    # 5桁目は1,2,3,4,5,6,7,8,9の9通り
    # 6桁目は1,2,3,4,5,6,7,8,9の9通り
    # 7桁目は1,2,3,4,5,6,7,8,9の9通り
    # 8桁目は1,2,3,4,5,6,7,8,9の9通り
    # 9桁目は1,2,3,4,5,6,7,8,9の9通り
    # 10桁目は1,2,3,4,5,6,7,8,9の9通り
    # 11桁目は1,2,3,4,5,6,7,8,9の9通り
    # 12桁目は1,2,3,4,5,6,7,8,9の9通り
    # 13桁目は1,2,3,4,5,6,7,8,9の9通り
    # 14桁目は1,2,3,4,5,6,7,8,9の9通り
    #
