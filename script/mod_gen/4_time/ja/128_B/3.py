def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        restaurant.append(input().split())
        restaurant[i][1] = int(restaurant[i][1])
        restaurant[i].append(i+1)
    restaurant.sort(key=lambda x:(x[0],-x[1]))
    for i in range(n):
        print(restaurant[i][2])

if __name__ == '__main__':
    main()