def get_input():
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurant = input().split()
        restaurants.append(restaurant)
    return N, restaurants
