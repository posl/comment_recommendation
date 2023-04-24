Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    data = []
    for i in range(N):
        s, p = input().split()
        data.append([s, int(p), i+1])
    data.sort(key=lambda x: (x[0], -x[1]))
    for d in data:
        print(d[2])

=======
Suggestion 2

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 3

def main():
    N = int(input())
    data = []
    for i in range(N):
        s, p = input().split()
        data.append([s, int(p), i+1])
    data.sort(key=lambda x:(x[0], -x[1]))
    for s, p, i in data:
        print(i)

=======
Suggestion 4

def solve():
    N = int(input())
    S = [0]*N
    P = [0]*N
    for i in range(N):
        S[i], P[i] = input().split()
        P[i] = int(P[i])
    for i in range(N):
        print(P.index(max(P))+1)
        P[P.index(max(P))] = -1

=======
Suggestion 5

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 6

def main():
    n = int(input())
    data = [input().split() for _ in range(n)]
    data = sorted(data, key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(data[i][2])

=======
Suggestion 7

def main():
    N = int(input())
    city = []
    for i in range(N):
        city.append(input().split())
    city.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(N):
        print(city.index(city[i])+1)

=======
Suggestion 8

def main():
    N = int(input())
    restaurants = [input().split() for _ in range(N)]
    restaurants = [[i+1, r[0], int(r[1])] for i, r in enumerate(restaurants)]
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    for r in restaurants:
        print(r[0])

=======
Suggestion 9

def main():
    N = int(input())
    # レストランの名前と点数を格納するリスト
    restaurant = []
    for i in range(N):
        # レストランの名前と点数を格納
        restaurant.append(input().split())
        # レストランの名前を格納
        restaurant[i][0] = restaurant[i][0] + ' ' + str(i + 1)
        # レストランの点数を格納
        restaurant[i][1] = int(restaurant[i][1])
    # レストランの名前を辞書順にソート
    restaurant.sort(key=lambda x: x[0])
    # レストランの点数を降順にソート
    restaurant.sort(key=lambda x: x[1], reverse=True)
    # レストランの名前を表示
    for i in range(N):
        print(restaurant[i][0].split()[1])
