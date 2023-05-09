def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((i+1, S, int(P)))
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    for restaurant in restaurants:
        print(restaurant[0])
