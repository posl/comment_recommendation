def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x: (-x[1], x[0]))
    for restaurant in restaurants:
        print(restaurant[2])

if __name__ == '__main__':
    main()