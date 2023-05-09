def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i+1))
    sorted_restaurants = sorted(restaurants, key=lambda x: (x[0], -x[1]))
    for restaurant in sorted_restaurants:
        print(restaurant[2])

if __name__ == '__main__':
    main()