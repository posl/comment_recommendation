Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    T.remove(T_max)
    T_max2 = max(T)
    print(S[T.index(T_max2)])

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_max = max(T)
    T_max_index = T.index(T_max)
    T[T_max_index] = 0
    T_second_max = max(T)
    T_second_max_index = T.index(T_second_max)
    print(S[T_second_max_index])

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_max = max(T)
    T.remove(T_max)
    T_second = max(T)
    print(S[T.index(T_second)])

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #問題文の通りに処理
    T.sort(reverse=True)
    print(S[T.index(T[1])])

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T.sort(reverse=True)
    print(S[T.index(T[1])])

=======
Suggestion 6

def main():
    n = int(input())
    mountain = []
    for i in range(n):
        s, t = input().split()
        mountain.append([s, int(t)])
    mountain.sort(key=lambda x: x[1], reverse=True)
    print(mountain[1][0])

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    print(S[T.index(sorted(T)[-2])])

=======
Suggestion 8

def main():
    n = int(input())
    list = []
    for i in range(n):
        s, t = input().split()
        list.append([s, int(t)])
    list.sort(key=lambda x: x[1], reverse=True)
    print(list[1][0])

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    T.sort(reverse=True)
    print(S[T.index(T[1])])
