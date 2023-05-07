def main():
    N, W = map(int, input().split())
    water = [0] * 200001
    for _ in range(N):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    for i in range(200000):
        water[i + 1] += water[i]
    if max(water) > W:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()