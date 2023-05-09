def main():
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    colors = set()
    for i in range(K):
        colors.add(candies[i])
    max_colors = len(colors)
    for i in range(N-K):
        colors.remove(candies[i])
        colors.add(candies[i+K])
        if len(colors) > max_colors:
            max_colors = len(colors)
    print(max_colors)

if __name__ == '__main__':
    main()