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
    T.pop(T.index(T_max))
    S.pop(T.index(T_max))
    print(S[T.index(max(T))])

=======
Suggestion 2

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 3

def main():
    n = int(input())
    lst = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        lst.append([t, s])
    lst.sort(reverse=True)
    print(lst[1][1])

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
    max1 = max(T)
    max2 = 0
    for i in range(N):
        if T[i] != max1:
            max2 = max(max2, T[i])
    for i in range(N):
        if T[i] == max2:
            print(S[i])

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
    # print(S)
    # print(T)
    max = T[0]
    max_idx = 0
    for i in range(1, N):
        if T[i] > max:
            max = T[i]
            max_idx = i
    # print(max, max_idx)
    max = T[0]
    for i in range(0, N):
        if T[i] > max and i != max_idx:
            max = T[i]
    # print(max)
    for i in range(0, N):
        if T[i] == max:
            print(S[i])

=======
Suggestion 6

def main():
    N = int(input())
    mtn = []
    for i in range(N):
        mtn.append(input().split())
    mtn.sort(key=lambda x: int(x[1]), reverse=True)
    print(mtn[1][0])

=======
Suggestion 7

def main():
    # Read data
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # Find the second highest mountain
    max1 = -1
    max2 = -1
    for i in range(N):
        if max1 < T[i]:
            max2 = max1
            max1 = T[i]
        elif max2 < T[i]:
            max2 = T[i]
    # Find the name of the second highest mountain
    for i in range(N):
        if T[i] == max2:
            print(S[i])
            return

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split())
        T.append(int(S[i][1]))
    T.sort()
    for i in range(N):
        if T[-2] == int(S[i][1]):
            print(S[i][0])
            break

=======
Suggestion 9

def main():
    n = int(input())
    s = [input().split() for i in range(n)]
    t = sorted(s, key=lambda x: int(x[1]), reverse=True)
    print(t[1][0])

=======
Suggestion 10

def main():
    #Enter your code here. Read input from STDIN. Print output to STDOUT
    N = int(input())
    lst = []
    for i in range(N):
        lst.append([x for x in input().split()])
        lst[i][1] = int(lst[i][1])
    lst.sort(key = lambda x:x[1], reverse = True)
    print(lst[1][0])
