def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, -int(p), i + 1))
    restaurants.sort()
    for s, p, i in restaurants:
        print(i)

if __name__ == '__main__':
    main()