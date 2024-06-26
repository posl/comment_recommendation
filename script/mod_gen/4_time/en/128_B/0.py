def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        p = int(p)
        restaurants.append((s, p, i+1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

if __name__ == '__main__':
    main()