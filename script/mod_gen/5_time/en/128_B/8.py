def main():
    # N = int(input())
    # restaurants = []
    # for i in range(N):
    #     restaurants.append(input().split())
    # restaurants.sort(key=lambda x: x[0])
    # restaurants.sort(key=lambda x: int(x[1]), reverse=True)
    # for i in range(N):
    #     print(restaurants[i][2])
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(N):
        print(restaurants[i][2])

if __name__ == '__main__':
    main()