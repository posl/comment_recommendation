def main():
    N, W = list(map(int, input().split()))
    water = [0] * 200001
    for _ in range(N):
        s, t, p = list(map(int, input().split()))
        water[s] += p
        water[t] -= p
    for i in range(1, len(water)):
        water[i] += water[i - 1]
        if water[i] > W:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()