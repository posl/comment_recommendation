Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(list(input().split()))
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 2

def main():
    n = int(input())
    mountains = []
    for _ in range(n):
        name, height = input().split()
        mountains.append([name, int(height)])
    mountains.sort(key=lambda x: -x[1])
    print(mountains[1][0])

=======
Suggestion 3

def main():
    n = int(input())
    mountains = []
    for _ in range(n):
        name, height = input().split()
        mountains.append((name, int(height)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 4

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())

    mountains = sorted(mountains, key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 5

def main():
    N = int(input())
    T = []
    S = []
    for i in range(N):
        s, t = input().split()
        T.append(int(t))
        S.append(s)
    T2 = sorted(T, reverse=True)
    print(S[T.index(T2[1])])

=======
Suggestion 6

def main():
    # input
    n = int(input())
    mountains = []
    for _ in range(n):
        mountains.append(list(input().split()))

    # compute
    mountains.sort(key=lambda x: int(x[1]), reverse=True)

    # output
    print(mountains[1][0])

=======
Suggestion 7

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 8

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        mountains.append([s, t])
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T.sort(reverse=True)
    for i in range(N):
        if T[1] == int(T[i]):
            print(S[i])
            break

=======
Suggestion 10

def main():
    # 標準入力から値を取得する
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        mountains.append([s, t])

    # 高さでソートする
    mountains.sort(key=lambda x: x[1], reverse=True)

    # 2番目に高い山の名前を出力
    print(mountains[1][0])
