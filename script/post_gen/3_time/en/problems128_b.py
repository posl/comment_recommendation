Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    data = []
    for i in range(N):
        S, P = input().split()
        data.append((S, int(P), i+1))
    data.sort(key=lambda x: (x[0], -x[1]))
    for d in data:
        print(d[2])

main()

=======
Suggestion 2

def main():
    n = int(input())
    data = []
    for i in range(n):
        s, p = input().split()
        data.append([s, -int(p), i+1])
    data.sort()
    for d in data:
        print(d[2])

=======
Suggestion 3

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split() + [i + 1])
    data.sort(key=lambda x: (x[0], -int(x[1])))
    for d in data:
        print(d[2])

=======
Suggestion 4

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, p = input().split()
        p = int(p)
        if s in d:
            d[s].append((-p, i+1))
        else:
            d[s] = [(-p, i+1)]
    for k in sorted(d.keys()):
        for p, i in sorted(d[k]):
            print(i)

=======
Suggestion 5

def main():
    N = int(input())
    d = {}
    for i in range(N):
        S, P = input().split()
        P = int(P)
        if S in d:
            d[S].append((P, i+1))
        else:
            d[S] = [(P, i+1)]
    for k, v in sorted(d.items()):
        for p, i in sorted(v, reverse=True):
            print(i)

=======
Suggestion 6

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x: (-x[1], x[0]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 7

def main():
    n = int(input())
    data = [input().split() for _ in range(n)]
    data = [(data[i][0], int(data[i][1]), i+1) for i in range(n)]
    data.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(data[i][2])

=======
Suggestion 8

def main():
    n = int(input())
    r = []
    for i in range(n):
        s, p = input().split()
        r.append([s, int(p), i + 1])
    r.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(n):
        print(r[i][2])

main()

=======
Suggestion 9

def main():
    n = int(input())
    A = []
    for i in range(n):
        s, p = input().split()
        A.append([s, int(p), i + 1])
    A.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(n):
        print(A[i][2])

=======
Suggestion 10

def main():
    n = int(input())
    restaurant_list = [input().split() for _ in range(n)]
    restaurant_list = [[restaurant_list[i][0], int(restaurant_list[i][1]), i+1] for i in range(n)]
    restaurant_list.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurant_list:
        print(restaurant[2])
