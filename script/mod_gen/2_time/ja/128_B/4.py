def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        restaurant.append([i+1, S, P])
    restaurant.sort(key=lambda x: (x[1], -x[2]))
    for i in range(N):
        print(restaurant[i][0])

if __name__ == '__main__':
    main()