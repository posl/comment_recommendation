Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        restaurants.append([i+1, S, P])
    restaurants.sort(key=lambda x: x[0])
    restaurants.sort(key=lambda x: x[2], reverse=True)
    restaurants.sort(key=lambda x: x[1])
    for i in range(N):
        print(restaurants[i][0])

=======
Suggestion 2

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i + 1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 3

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: x[0])
    restaurants.sort(key=lambda x: int(x[1]), reverse=True)
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 4

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 5

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 6

def solve():
    N = int(input())
    S = []
    P = []
    for _ in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in range(N):
        print(P.index(sorted(P, reverse=True)[i]) + 1)

=======
Suggestion 7

def main():
    restaurants = []
    for i in range(int(input())):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 8

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
Suggestion 9

def main():
    # N = int(input())
    # restaurants = []
    # for i in range(N):
    #     restaurants.append(input().split())
    # restaurants.sort(key=lambda x: x[0])
    # restaurants.sort(key=lambda x: int(x[1]), reverse=True)
    # for i in range(N):
    #     print(restaurants[i][2])
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 10

def get_input():
    return input()
