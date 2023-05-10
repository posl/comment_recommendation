def main():
    n = int(input())
    heights = list(map(int, input().split()))
    max_height = heights[0]
    for i in range(1, n):
        if heights[i] > max_height:
            max_height = heights[i]
    print(max_height)

if __name__ == '__main__':
    main()