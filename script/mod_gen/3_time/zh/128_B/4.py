def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurant = input().split()
        restaurants.append((restaurant[0], int(restaurant[1]), i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

if __name__ == '__main__':
    main()