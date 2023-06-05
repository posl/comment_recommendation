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
