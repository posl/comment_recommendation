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
