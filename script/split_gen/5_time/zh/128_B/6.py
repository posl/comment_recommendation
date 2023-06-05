def input():
    n = int(raw_input())
    restaurants = []
    for i in range(n):
        restaurants.append(raw_input().split())
    return n, restaurants
