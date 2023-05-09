def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append([i+1, S, int(P)])
    restaurants.sort(key=lambda x: x[2], reverse=True)
    restaurants.sort(key=lambda x: x[1])
    for i in restaurants:
        print(i[0])

if __name__ == '__main__':
    main()