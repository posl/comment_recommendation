def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        s, p = input().split()
        restaurant.append([s, int(p), i + 1])
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurant[i][2])

if __name__ == '__main__':
    main()