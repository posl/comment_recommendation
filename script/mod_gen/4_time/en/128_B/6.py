def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurant = input().split()
        restaurants.append([restaurant[0], int(restaurant[1]), i+1])
    restaurants.sort(key=lambda x:x[1], reverse=True)
    restaurants.sort(key=lambda x:x[0])
    for r in restaurants:
        print(r[2])

if __name__ == '__main__':
    main()