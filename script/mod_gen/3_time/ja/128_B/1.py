def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append([s, int(p), i + 1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurants[i][2])

if __name__ == '__main__':
    main()