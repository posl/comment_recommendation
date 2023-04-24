Synthesizing 10/10 solutions

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
    print(S[T.index(max(T))])

=======
Suggestion 2

def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])

=======
Suggestion 3

def main():
    N = int(input())
    mountain = [input().split() for _ in range(N)]
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])

=======
Suggestion 4

def main():
    N = int(input())
    mountain_list = []
    for i in range(N):
        mountain_list.append(input().split())
    mountain_list.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain_list[1][0])

=======
Suggestion 5

def main():
    n = int(input())
    mountain_list = []
    for i in range(n):
        mountain_list.append(input().split())
    mountain_list.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain_list[1][0])

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    max_T = max(T)
    max_T_index = T.index(max_T)
    T[max_T_index] = 0
    max_T = max(T)
    print(S[T.index(max_T)])

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T2 = sorted(T, reverse=True)
    print(S[T.index(T2[1])])

=======
Suggestion 8

def main():
    n = int(input())
    mountain = []
    for i in range(n):
        s, t = input().split()
        mountain.append((s, int(t)))

    mountain = sorted(mountain, key=lambda x: x[1], reverse=True)
    print(mountain[1][0])

=======
Suggestion 9

def main():
    N = int(input())
    mnt = []
    for i in range(N):
        s, t = input().split()
        mnt.append([s, int(t)])
    mnt.sort(key=lambda x: x[1], reverse=True)
    print(mnt[1][0])

=======
Suggestion 10

def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key = lambda x: int(x[1]))
    print(mountain[N-2][0])
