def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append([S, int(P), i + 1])
    restaurants.sort(key=lambda x:(x[0], -x[1]))
    for i in range(N):
        print(restaurants[i][2])

if __name__ == '__main__':
    main()