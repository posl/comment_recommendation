Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if 4*i + 7*j == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if 4*i + 7*j == N:
                print("Yes")
                return
    print("No")

main()

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            if 4 * i + 7 * j == n:
                print("Yes")
                return
    print("No")

main()

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(0, N//4+1):
        for j in range(0, N//7+1):
            if 4*i + 7*j == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 5

def main():
    N = int(input())
    if N == 1 or N == 2 or N == 3 or N == 5 or N == 6:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%4 == 7 or n%7 == 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(N//4+1):
        if (N-4*i)%7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    n = int(input())
    flag = False
    for i in range(n+1):
        if i*4 + (n-i)*7 == n:
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N = int(input())
    # N = 11
    # N = 40
    # N = 3

    # 1 個 4 ドルのケーキと 1 個 7 ドルのドーナツの合計金額が N ドルとなる買い方があるかどうかを判定する
    # 4 ドルのケーキを i 個, 7 ドルのドーナツを j 個買うと, 合計金額は 4 × i + 7 × j ドルとなる
    # 4 × i + 7 × j = N となる i, j を求める
    # 4 × i + 7 × j = N
    # 7 × j = N - 4 × i
    # j = (N - 4 × i) / 7
    # 7 × j が整数かどうかで判定する
    for i in range(0, N + 1):
        if (N - 4 * i) % 7 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    N = int(input())
    for i in range(100):
        if 4*i <= N and (N - 4*i)%7 == 0:
            print("Yes")
            return
    print("No")
