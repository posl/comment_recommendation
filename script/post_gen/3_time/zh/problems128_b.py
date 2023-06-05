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
    for r in restaurants:
        print(r[2])

=======
Suggestion 2

def input():
    n = int(raw_input())
    s = []
    p = []
    for i in range(n):
        line = raw_input().split()
        s.append(line[0])
        p.append(line[1])
    return n, s, p

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        s, p = input().split()
        a.append([s, int(p), i + 1])
    a.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(a[i][2])

=======
Suggestion 4

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input().split())
    arr.sort(key=lambda x: (-int(x[1]), x[0]))
    for i in range(n):
        print(arr[i][0])

=======
Suggestion 5

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurants.append((restaurant[0], int(restaurant[1]), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 6

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        p = int(p)
        restaurants.append([i+1, s, p])
    restaurants.sort(key=lambda x: (x[1], -x[2]))
    for i in range(n):
        print(restaurants[i][0])

=======
Suggestion 7

def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        s, p = input().split()
        restaurant.append((s, int(p), i + 1))
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurant:
        print(r[2])

=======
Suggestion 8

def sort_by_name(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j][0] > list[j+1][0]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

=======
Suggestion 9

def sort_by_city_and_score(data):
    data.sort(key=lambda x: x[0])
    data.sort(key=lambda x: x[1], reverse=True)
    return data

=======
Suggestion 10

def main():
    n = int(input())
    s_p_list = []
    for i in range(n):
        s, p = input().split()
        s_p_list.append((s, int(p)))
    s_p_list.sort(key=lambda x: x[0])
    s_p_list.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(i + 1)
