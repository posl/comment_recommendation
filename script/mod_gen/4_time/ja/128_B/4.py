def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        S, P = input().split()
        restaurant.append((S, int(P), i+1))
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(restaurant[i][2])

if __name__ == '__main__':
    main()