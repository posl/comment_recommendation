def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for restaurant in restaurants:
        print(restaurant[2])

if __name__ == '__main__':
    main()