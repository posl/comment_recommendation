Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurant = input().split()
        restaurants.append(restaurant)
    return N, restaurants

=======
Suggestion 2

def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        s, p = input().split()
        restaurant.append([s, int(p), i+1])
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurant:
        print(r[2])

=======
Suggestion 3

def getkey(item):
    return item[1]

N = int(input())
a = []

for i in range(N):
    s, p = input().split()
    a.append([i+1, s, int(p)])

a.sort(key=getkey, reverse=True)
a.sort(key=lambda x:x[1])

for i in range(N):
    print(a[i][0])

=======
Suggestion 4

def solve():
    n = int(input())
    data = []
    for i in range(n):
        s, p = input().split()
        data.append((s, int(p)))
    data.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(data[i][1])

=======
Suggestion 5

def get_input():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurant[1] = int(restaurant[1])
        restaurants.append(restaurant)
    return restaurants

=======
Suggestion 6

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 7

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurants.append((restaurant[0],int(restaurant[1]),i+1))
    restaurants.sort(key=lambda x:(x[0],-x[1]))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 8

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurant[1] = int(restaurant[1])
        restaurant.append(i + 1)
        restaurants.append(restaurant)
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 9

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2] + 1)

=======
Suggestion 10

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P)))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurants.index(restaurant) + 1)
