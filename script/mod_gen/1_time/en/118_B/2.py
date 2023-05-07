def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        for food in map(int, input().split()[1:]):
            foods[food - 1] += 1
    print(len([food for food in foods if food == N]))

if __name__ == '__main__':
    main()