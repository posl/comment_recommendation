def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        for food in map(int, input().split()[1:]):
            foods[food - 1] += 1
    print(foods.count(N))

if __name__ == '__main__':
    main()