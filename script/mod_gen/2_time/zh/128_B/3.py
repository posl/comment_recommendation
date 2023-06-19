def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        name, score = input().split()
        restaurants.append([name, int(score)])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(restaurants[i][1])

if __name__ == '__main__':
    main()