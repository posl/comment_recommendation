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
    print(S[T.index(sorted(T)[-2])])

=======
Suggestion 2

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
    T_max = max(T)
    print(S[T.index(T_max)])

=======
Suggestion 3

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split()
        mountains.append([name, int(height)])
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_sorted = sorted(T, reverse = True)
    second_highest = T_sorted[1]
    for i in range(N):
        if T[i] == second_highest:
            print(S[i])
            break

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
    T_sort = sorted(T, reverse=True)
    print(S[T.index(T_sort[1])])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(int(ti))
    t_max = max(t)
    t.remove(t_max)
    s_max = s[t.index(max(t))]
    print(s_max)

=======
Suggestion 7

def main():
    #input
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = map(str, input().split())
        S.append(s)
        T.append(int(t))
    #process
    t_max = max(T)
    T.remove(t_max)
    t_max2 = max(T)
    i_max2 = T.index(t_max2)
    #output
    print(S[i_max2])

=======
Suggestion 8

def main():
    N = int(input())
    mountain = {}
    for _ in range(N):
        s, t = input().split()
        mountain[s] = int(t)
    mountain = sorted(mountain.items(), key=lambda x: x[1], reverse=True)
    print(mountain[1][0])

=======
Suggestion 9

def main():
    mountain = []
    N = int(input())
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])
