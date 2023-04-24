Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    T2 = sorted(T)
    print(S[T.index(T2[-2])])

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
    T_max2 = max(T)
    print(S[T.index(T_max2)])

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    T[T.index(T_max)] = 0
    T_2nd = max(T)
    print(S[T.index(T_2nd)])

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
    
    #ソート
    T_sort = sorted(T, reverse=True)
    
    #出力
    print(S[T.index(T_sort[1])])

=======
Suggestion 5

def main():
    N = int(input())
    mountain = []
    for i in range(N):
        S, T = input().split()
        mountain.append((S, int(T)))
    mountain.sort(key=lambda x: x[1])
    print(mountain[-2][0])

=======
Suggestion 6

def main():
    N = int(input())
    d = {}
    for i in range(N):
        S, T = map(str, input().split())
        d[S] = int(T)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d[1][0])

=======
Suggestion 7

def main():
    N = int(input())
    name = []
    height = []
    for i in range(N):
        name.append(input().split()[0])
        height.append(int(input().split()[1]))
    #print(name)
    #print(height)
    max1 = max(height)
    #print(max1)
    max1_index = height.index(max1)
    #print(max1_index)
    del height[max1_index]
    max2 = max(height)
    #print(max2)
    max2_index = height.index(max2)
    #print(max2_index)
    print(name[max2_index])

=======
Suggestion 8

def main():
    N = int(input())
    S_T = []
    for i in range(N):
        S_T.append(input().split())

    T = []
    for i in range(N):
        T.append(int(S_T[i][1]))

    T.sort(reverse=True)

    for i in range(N):
        if int(S_T[i][1]) == T[1]:
            print(S_T[i][0])

=======
Suggestion 9

def main():
    n = int(input())
    m = {}
    for i in range(n):
        s, t = input().split()
        m[s] = int(t)
    #print(m)
    m = sorted(m.items(), key=lambda x:x[1], reverse=True)
    print(m[1][0])

=======
Suggestion 10

def main():
    # 入力
    N = int(input())
    S_T = [input().split() for _ in range(N)]
    # 高さを整数に変換
    S_T = [[S, int(T)] for S, T in S_T]
    # 高さを基準にソート
    S_T.sort(key=lambda x: x[1], reverse=True)
    # 出力
    print(S_T[1][0])
