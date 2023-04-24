Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i + 1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 2

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i+1))
    restaurants.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 3

def main():
    N = int(input())
    data = []
    for i in range(N):
        S, P = input().split()
        data.append([S, int(P), i+1])
    data.sort(key=lambda x: (-x[1], x[0]))
    for i in data:
        print(i[2])

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    P = []
    for _ in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in sorted(range(N), key=lambda i: (-P[i], S[i])):
        print(i + 1)

=======
Suggestion 5

def main():
    n = int(input())
    r = []
    for i in range(n):
        s, p = input().split()
        r.append((s, int(p), i + 1))
    r.sort(key=lambda x: (-x[1], x[0]))
    for i in range(n):
        print(r[i][2])

=======
Suggestion 6

def main():
    N = int(input())
    city = [0]*N
    score = [0]*N
    for i in range(N):
        city[i], score[i] = input().split()
        score[i] = int(score[i])
    for i in range(N):
        print(score.index(max(score))+1)
        score[score.index(max(score))] = -1

=======
Suggestion 7

def main():
    n = int(input())
    list = []
    for i in range(n):
        s, p = input().split()
        list.append((s, int(p), i + 1))
    list.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(list[i][2])

=======
Suggestion 8

def main():
    N = int(input())
    city = []
    for i in range(N):
        S, P = input().split()
        city.append([S, int(P), i+1])
    city.sort(key=lambda x: (x[0], -x[1]))
    for i in city:
        print(i[2])

=======
Suggestion 9

def main():
    N = int(input())
    S = [input().split() for _ in range(N)]

    for i in range(N):
        S[i][1] = int(S[i][1])

    S.sort(key=lambda x: x[0])
    S.sort(key=lambda x: x[1], reverse=True)

    for i in range(N):
        print(S[i][0])

=======
Suggestion 10

def main():
    N = int(input())
    rest_list = []
    for i in range(N):
        rest_list.append(input().split())
    rest_list.sort(key = lambda x: x[0])
    rest_list.sort(key = lambda x: int(x[1]), reverse = True)
    for i in range(N):
        print(rest_list[i][2])
