Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        restaurant.append(input().split())
    restaurant.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(restaurant[i][2])

=======
Suggestion 2

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurants.append(input().split())
    restaurants.sort(key = lambda x: (x[0],-int(x[1])))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 3

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((i+1, s, int(p)))
    restaurants.sort(key=lambda x: (x[1], -x[2]))
    for restaurant in restaurants:
        print(restaurant[0])

=======
Suggestion 4

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        city, score = input().split()
        restaurants.append((city, int(score), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 5

def main():
    n = int(input())
    # restaurants = []
    # for i in range(n):
    #     restaurants.append(input().split())
    restaurants = [input().split() for i in range(n)]
    restaurants.sort(key=lambda x: x[0])
    restaurants.sort(key=lambda x: int(x[1]), reverse=True)
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 6

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 7

def input():
    n = int(raw_input())
    restaurants = []
    for i in range(n):
        restaurants.append(raw_input().split())
    return n, restaurants

=======
Suggestion 8

def main():
    # 读取数据
    num = int(input())
    data = []
    for i in range(num):
        data.append(input().split())
    # 数据处理
    data.sort(key=lambda x: (x[0], -int(x[1])))
    # 输出结果
    for i in range(num):
        print(data[i][0], data[i][1])

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        S.append(input().split()[0])
        P.append(int(input().split()[1]))
    for i in range(N):
        for j in range(N-i-1):
            if S[j] > S[j+1]:
                S[j],S[j+1] = S[j+1],S[j]
                P[j],P[j+1] = P[j+1],P[j]
            elif S[j] == S[j+1]:
                if P[j] < P[j+1]:
                    P[j],P[j+1] = P[j+1],P[j]
    for i in range(N):
        print(P[i])

=======
Suggestion 10

def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        S, P = input().split()
        restaurant.append([S, int(P), i+1])
    restaurant.sort(key=lambda x:(x[0], -x[1]))
    for i in range(N):
        print(restaurant[i][2])
