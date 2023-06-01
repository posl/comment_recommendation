Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

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

def get_input():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    return N, mountain

=======
Suggestion 4

def second_height():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    T_sort = sorted(T)
    for i in range(N):
        if T[i] == T_sort[-2]:
            print(S[i])
            break

=======
Suggestion 5

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split()
        mountains.append((name, int(height)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 6

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains = sorted(mountains, key=lambda x:int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 7

def second_highest_mountain():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())
    mountains.sort(key=lambda x:int(x[1]),reverse=True)
    print(mountains[1][0])

=======
Suggestion 8

def problems201_b():
    n = int(input())
    data = [input().split() for _ in range(n)]
    data = sorted(data, key=lambda x: int(x[1]), reverse=True)
    print(data[1][0])
