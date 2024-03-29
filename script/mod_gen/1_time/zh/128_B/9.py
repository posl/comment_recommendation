def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i))
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0])
    for i in range(n):
        print(restaurants[i][2] + 1)

if __name__ == '__main__':
    main()