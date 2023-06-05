def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P)))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurants.index(restaurant) + 1)
