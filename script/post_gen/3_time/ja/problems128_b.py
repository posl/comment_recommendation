Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i + 1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 3

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append([s, int(p), i + 1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 4

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s,p = input().split()
        p = int(p)
        restaurants.append((s,p,i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurants:
        print(r[2])

=======
Suggestion 5

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append([S, int(P), i + 1])
    restaurants.sort(key=lambda x:(x[0], -x[1]))
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 6

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append([i+1, s, int(p)])

    restaurants.sort(key=lambda x: (x[1], -x[2]))
    for restaurant in restaurants:
        print(restaurant[0])

=======
Suggestion 7

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(restaurants[i][2])

=======
Suggestion 8

def main():
    N = int(input())
    data = []
    for i in range(N):
        S,P = input().split()
        data.append((S,int(P),i+1))
    data.sort(key=lambda x:(x[0],-x[1]))
    for i in range(N):
        print(data[i][2])

=======
Suggestion 9

def solve():
    # 入力
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append([i + 1, S, int(P)])

    # 処理
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))

    # 出力
    for restaurant in restaurants:
        print(restaurant[0])

=======
Suggestion 10

def input():
    return sys.stdin.readline()[:-1]

import sys
import collections

N = int(input())

restaurants = []
for i in range(N):
    S, P = input().split()
    restaurants.append((S, int(P), i + 1))

restaurants.sort(key=lambda x: x[1], reverse=True)
restaurants.sort(key=lambda x: x[0])

for restaurant in restaurants:
    print(restaurant[2])
