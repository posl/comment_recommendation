def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((i+1, s, int(p)))
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    for i in range(n):
        print(restaurants[i][0])

if __name__ == '__main__':
    main()