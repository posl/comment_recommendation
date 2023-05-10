def main():
    n = int(input())
    heights = list(map(int, input().split()))
    count = 1
    max_height = heights[0]
    for i in range(1, n):
        if heights[i] >= max_height:
            count += 1
            max_height = heights[i]
    print(count)

if __name__ == '__main__':
    main()