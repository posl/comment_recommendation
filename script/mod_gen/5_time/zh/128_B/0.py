def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        restaurant.append(input().split())
    restaurant.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(restaurant[i][2])

if __name__ == '__main__':
    main()