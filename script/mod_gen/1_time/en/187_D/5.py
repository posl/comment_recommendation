def main():
    n = int(input())
    town = []
    for i in range(n):
        a, b = map(int, input().split())
        town.append([a, b])
    town = sorted(town, key=lambda x: x[0] + x[1], reverse=True)
    takahashi = 0
    aoki = 0
    result = 0
    for i in range(n):
        takahashi += town[i][0]
        aoki += town[i][1]
        result += 1
        if takahashi > aoki:
            break
    print(result)

if __name__ == '__main__':
    main()