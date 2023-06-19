Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    num = int(input())
    rest = []
    for i in range(num):
        name, score = input().split()
        rest.append([name, int(score)])
    rest = sorted(rest, key=lambda x: (x[0], -x[1]))
    for i in range(num):
        print(rest[i][1])

=======
Suggestion 2

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x:(x[0],-x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 3

def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        s, p = input().split()
        restaurant.append([s, int(p), i + 1])
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurant[i][2])

=======
Suggestion 4

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        name, score = input().split()
        restaurants.append([name, int(score)])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurants[i][1])

=======
Suggestion 5

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i + 1])
    restaurants.sort()
    restaurants.sort(key=lambda x: x[1], reverse=True)
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 6

def print_restaurant_list(restaurant_list):
    for restaurant in restaurant_list:
        print(restaurant[2])

=======
Suggestion 7

def get_city_and_score():
    city_and_score = {}
    num = int(input())
    for i in range(num):
        city, score = input().split()
        city_and_score[city] = int(score)
    return city_and_score

=======
Suggestion 8

def get_key(x):
    return x[1]

=======
Suggestion 9

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, p = input().split()
        p = int(p)
        if s in d:
            d[s].append(p)
        else:
            d[s] = [p]
    for k in sorted(d.keys()):
        for v in sorted(d[k], reverse=True):
            print(v)

=======
Suggestion 10

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        city, point = input().split()
        restaurants.append((city, int(point)))
    restaurants.sort(key=lambda x: x[0])
    restaurants.sort(key=lambda x: x[1], reverse=True)
    for restaurant in restaurants:
        print(restaurants.index(restaurant) + 1)
