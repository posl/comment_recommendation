def main():
    N = int(input())
    restaurants = [input().split() for _ in range(N)]
    restaurants = [[i+1, r[0], int(r[1])] for i, r in enumerate(restaurants)]
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    for r in restaurants:
        print(r[0])

if __name__ == '__main__':
    main()