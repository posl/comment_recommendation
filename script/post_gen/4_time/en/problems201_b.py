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
    T_max = max(T)
    T[T.index(T_max)] = 0
    print(S[T.index(max(T))])

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
    for i in range(N):
        if T[i] == T_max:
            T[i] = 0
    T_second = max(T)
    for i in range(N):
        if T[i] == T_second:
            print(S[i])
            break

=======
Suggestion 3

def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain = sorted(mountain, key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])

=======
Suggestion 4

def main():
    n = int(input())
    mountain = []
    for i in range(n):
        mountain.append(list(map(str, input().split())))
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))

    max = 0
    second = 0
    index = 0
    for i in range(N):
        if max < T[i]:
            max = T[i]
            index = i
    for i in range(N):
        if second < T[i] and i != index:
            second = T[i]
    print(S[index])

=======
Suggestion 6

def main():
    n = int(input())
    mountains = {}
    for i in range(n):
        s, t = input().split()
        mountains[s] = int(t)
    print(sorted(mountains, key=mountains.get)[-2])

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    T.sort()
    for i in range(N):
        if T[N-2] == int(input().split()[1]):
            print(S[i])
            break

=======
Suggestion 8

def main():
    N = int(input())
    A = [input().split() for _ in range(N)]
    A = sorted(A, key = lambda x: x[1], reverse=True)
    print(A[1][0])

=======
Suggestion 9

def main():
    #Read the first line.
    N = int(input())
    #Read the next N lines.
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #Find the index of the second highest mountain.
    index_max = T.index(max(T))
    T[index_max] = 0
    index_second_max = T.index(max(T))
    #Print the name of the second highest mountain.
    print(S[index_second_max])

=======
Suggestion 10

def getSecondHighestMountainName():
    N = int(input())
    mountainNameHeightList = []
    for i in range(N):
        mountainNameHeightList.append(input().split())
    mountainNameHeightList.sort(key=lambda x: x[1], reverse=True)
    return mountainNameHeightList[1][0]
