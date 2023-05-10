def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i + 1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for _, _, i in restaurants:
        print(i)

if __name__ == '__main__':
    main()