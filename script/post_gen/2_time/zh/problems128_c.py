Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split(' '))
    return n, data

=======
Suggestion 2

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
    for k in sorted(d):
        for v in sorted(d[k], reverse=True):
            print(d[k].index(v)+1)

=======
Suggestion 3

def main():
    n = int(input())
    rest = []
    for i in range(n):
        s, p = input().split()
        rest.append((s, 100 - int(p), i + 1))
    rest.sort()
    rest.sort(key=lambda x: x[1])
    for i in rest:
        print(i[2])

=======
Suggestion 4

def main():
    n = int(input())
    #city = []
    #score = []
    #for i in range(n):
    #    c,s = input().split()
    #    city.append(c)
    #    score.append(s)
    #city_score = zip(city,score)
    #city_score = sorted(city_score, key=lambda x: x[0])
    #city_score = sorted(city_score, key=lambda x: x[1], reverse=True)
    #for i in range(n):
    #    print(city_score[i][0])
    city_score = []
    for i in range(n):
        c,s = input().split()
        city_score.append((c,s))
    city_score.sort(key=lambda x: x[0])
    city_score.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(city_score[i][0])

=======
Suggestion 5

def main():
    n = int(input())
    list1 = []
    for i in range(n):
        s, p = input().split()
        list1.append((s, int(p)))
    list1.sort(key=lambda x: x[1], reverse=True)
    list1.sort(key=lambda x: x[0])
    for i in list1:
        print(list1.index(i) + 1)

=======
Suggestion 6

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        city, score = input().split()
        restaurants.append((city, int(score), i + 1))
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0])
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 7

def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append((s, int(p), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 8

def main():
    n = int(input())
    lst = []
    for i in range(n):
        s, p = input().split()
        lst.append((s, int(p), i + 1))
    lst.sort(key=lambda x: (x[0], -x[1]))
    for item in lst:
        print(item[2])

=======
Suggestion 9

def main():
    n = int(input())
    res = []
    for i in range(n):
        s, p = input().split()
        res.append([s, int(p), i+1])
    res.sort(key=lambda x: (x[0], -x[1]))
    for i in res:
        print(i[2])

=======
Suggestion 10

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i))
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0])
    for i in range(n):
        print(restaurants[i][2] + 1)
