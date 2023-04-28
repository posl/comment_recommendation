Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        p = int(p)
        restaurants.append((s, p, i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 2

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((i+1, S, int(P)))
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    for restaurant in restaurants:
        print(restaurant[0])

=======
Suggestion 3

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((i+1, s, int(p)))
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    for i in range(n):
        print(restaurants[i][0])

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 6

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i + 1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 7

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurant = input().split()
        restaurants.append([restaurant[0], int(restaurant[1]), i+1])
    restaurants.sort(key=lambda x:x[1], reverse=True)
    restaurants.sort(key=lambda x:x[0])
    for r in restaurants:
        print(r[2])

=======
Suggestion 8

def main():
    n = int(input())
    s_p = []
    for i in range(n):
        s, p = input().split()
        p = int(p)
        s_p.append((s, p, i+1))
    s_p.sort(key=lambda x: (x[0], -x[1]))
    for s, p, i in s_p:
        print(i)

=======
Suggestion 9

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((i + 1, s, int(p)))

    restaurants.sort(key=lambda x: (x[1], -x[2]))

    for restaurant in restaurants:
        print(restaurant[0])

=======
Suggestion 10

def main():
    # Get input
    n = int(input())
    restaurants = []
    for i in range(n):
        city, score = input().split()
        restaurants.append([city, int(score), i+1])
    # Sort the list
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    # Print the result
    for restaurant in restaurants:
        print(restaurant[2])
