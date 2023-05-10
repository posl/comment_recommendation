def main():
    num_candies, num_consecutive = map(int, input().split())
    candies = list(map(int, input().split()))
    max_colors = 0
    for i in range(num_candies-num_consecutive+1):
        max_colors = max(max_colors, len(set(candies[i:i+num_consecutive])))
    print(max_colors)

if __name__ == '__main__':
    main()