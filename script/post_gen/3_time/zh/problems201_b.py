Synthesizing 10/10 solutions

=======
Suggestion 1

def func():
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
    mountains = []
    for i in range(N):
        S, T = input().split()
        mountains.append((S, int(T)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 3

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains = sorted(mountains, key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 4

def get_second_highest_mountain_name(mountain_list):
    highest_mountain = mountain_list[0]
    second_highest_mountain = mountain_list[0]
    for mountain in mountain_list:
        if mountain[1] > highest_mountain[1]:
            second_highest_mountain = highest_mountain
            highest_mountain = mountain
        elif mountain[1] > second_highest_mountain[1]:
            second_highest_mountain = mountain
    return second_highest_mountain[0]

=======
Suggestion 5

def main():
    N = int(input())
    T = []
    S = []
    for i in range(N):
        s,t = input().split()
        T.append(int(t))
        S.append(s)
    T2 = sorted(T,reverse=True)[1]
    print(S[T.index(T2)])

=======
Suggestion 6

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append([S, T])
    mountains.sort(key=lambda x: x[1], reverse=True)
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
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])

=======
Suggestion 9

def problems201_b():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: -int(x[1]))
    print(mountains[1][0])

=======
Suggestion 10

def get_second_highest_mountain_name():
    dict = {}
    n = int(input())
    for i in range(n):
        s, t = input().split()
        dict[s] = int(t)
    sorted_dict = sorted(dict.items(), key=lambda d: d[1], reverse=True)
    return sorted_dict[1][0]

print(get_second_highest_mountain_name())
