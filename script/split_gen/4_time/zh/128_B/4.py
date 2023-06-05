def get_input():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurant[1] = int(restaurant[1])
        restaurants.append(restaurant)
    return restaurants
